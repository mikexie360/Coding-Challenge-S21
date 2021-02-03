#***********************************************************************
# File: genbankParser.py
# Author: Mike Xie
# Procedures:
# genbankParser 	- parse a genbank file and output a circular genome map in an image file
#**********************************************************************

import os

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqUtils import GC

from Bio.Graphics.GenomeDiagram import FeatureSet, GraphSet, Track, Diagram
from Bio.Graphics.GenomeDiagram._Graph import GraphData

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO, GenBank

# function definition of main
# we will be using a top down approach
# first parse the genbank file and then create an empty diagram
# second, add an empty track, and then an empty feature set
# third, add all the features into the feature set
# fourth, draw all the shapes
# fifth, save all the drawings into different file formats
def genbankParser():
	# parse the genbank file
	record = SeqIO.read("Genome.gb", "genbank")

	# create an empty diagram
	gd_diagram = GenomeDiagram.Diagram(record.description)
	
	# add an empty track
	gd_track1_for_features = gd_diagram.new_track(1, greytrack=1, name="Annotated features")
	gd_track3_for_features = gd_diagram.new_track(3, greytrack=1, name="Graph content")

	# add an empty feature and graph set
	gd_feature_set1 = gd_track1_for_features.new_set('feature')
	gd_feature_set3 = gd_track3_for_features.new_set('graph')

	# add a new graph to the graph set
	graphData = [(f.location.start,GC(f.extract(record.seq))) for f in record.features]
	gd_feature_set3.new_graph(graphData,"Graph content",color=colors.red,altcolor=colors.green)


	# add the features into the feature set
	for feature in record.features:
		if feature.type != "gene":
			# Exclude Non genes features
			continue
		if len(gd_feature_set1) % 2 == 0:
			color = colors.red
		else:
			color = colors.green
		gd_feature_set1.add_feature(feature=feature, color=color,label=True)

	# call the draw method to create all the shapes
	gd_diagram.draw(
		format="circular",
		circular=True,
		orientation = "landscape",
		tracklines=False,
		pagesize="A4",
		fragments=5,
		start=0,
		end=len(record),
		circle_core=0.7,
	)

	# call the write method to render the requested file formats
	gd_diagram.write(record.description+".jpg", "JPG")
	gd_diagram.write(record.description+".svg", "SVG")
	gd_diagram.write(record.description+".png", "PNG")

genbankParser()