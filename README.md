# genbankParser.py

The python script called genbankParser.py is a script that parses a genbank file and outputs a circular genome map. It outputs the circular genome map as a JPG, SVG and PNG image files.

To use the script, place a file called "Genome.gb" inside the same directory as the genbankParser.py program.

genbankParser.py works by first parsing the "Genome.gb" file as a genbank file fromat using SeqIO.read() function.
It will then create an empty diagram and two empty tracks for the diagram. The first track will be populated with gene feature sets and the second track will be populated from the gene sequence. Once all tracks have been populated with features, the program will draw the image and save the image to files.

## Libraries
This python script mainly uses the Biopython library, and the reportlab library. genbankParser.py uses the Biopython library for parsing the genbank files and creating the drawings and image. The reportlab library generates the colors for the image.

## How I solved Question One
I solve coding challenges by first reading the challenge carefully and researching topics the challenge introduces. In this case I do not know what a genbank file and circular genome map were when first starting the challenge. I researched what genbank files were and what a circular genome map looked like.

Once I have done my research on the initial topic, I work out what my code needs to do to successfully solve the coding challenge. My code would need to take in a .gb file as input and parse it, and then output an image file of a circular genome map.

After that, I research possible tools to help write my code. In this case, the coding challenge gave a useful hint to use python. So I researched python libraries to help parse genbank files and make circular genome maps. This is when I did research on the Biopython library and found out how useful it was.

And then, I tried to follow the documentation and tutorials of Biopython to write the python script for the coding challenge.

Finally, I test and run. If the code does work, I comment my code and write the documentation for the script.

## References
http://biopython.org/DIST/docs/tutorial/Tutorial.html
https://biopython.org/docs/1.75/api/Bio.html
https://www.reportlab.com/
