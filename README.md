# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

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
