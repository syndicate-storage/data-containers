# Mash

This image contains Mash, a bioinformatics tool. Use the following command to 
execute the image.

```
docker run -ti --privileged <image_name>
```

Public dataset is automatically mounted on `/opt/dataset` once the image 
is successfully launched.

Mash computes genetic distances between DNA sequence files in FASTA format. 
FASTA files usually have following filename suffix:
- fa
- ffn
- fna
- faa
- fasta
- fas
- fsa
- seq

Mash has two stages, 1) sketch and 2) distance calculation. 

To sketch DNA sequence files, type:
```
mash sketch -o <sketch_output> <sequence_input>
```

To calculate distance, type:
```
mash dist <sketch_output1> <sketch_output2>
```
The command will compare sequence files in `sketch_output1` and sequence files
in `sketch_output2`.

Often, we do pair-wise comparisons between all sequence files in a directory. In
such case, do self-comparison.
```
mash dist <sketch_output> <sketch_output>
```
