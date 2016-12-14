#!/bin/bash

version=1.0

##arguments
help(){
	echo "Programm:"
	echo "bamtobw_zp.sh --- convert the bam to bw file"
	echo ""
	echo "Usage:"
	echo "bash bamtobw_zp.sh <option>* [-i inputfilename] [-o outputpath] [-c chromsize]"
	echo ""
	echo "Tips"
	echo "inputfilename is name of file (eg:if the file is seq.bam just write seq here)"
	echo "outputpath is end by /"
}

if [ $# -lt 3 ];
then
	help
	exit 1
fi

while getopts "i:o:c:" Arg
do
	case $Arg in
		i)	inputfilename=$OPTARG;;
		o)	outputpath=$OPTARG;;
		c)	chromsize=$OPTARG;;
		?)	echo "check parameters!"
			exit 1;;
	esac
done

echo "start	" `date +%Y-%m-%d\ %H:%M:%S`
echo "samtools sort------"
samtools sort $inputfilename".bam" $inputfilename"_sorted"
echo "samtools depth and convert to wig-------"
samtools depth $inputfilename"_sorted.bam" | perl -ne 'BEGIN{ print "track type=print wiggle_0 name=fileName description=fileName\n"}; ($c, $start, $depth) = split;if ($c ne $lastC) { print "variableStep chrom=$c span=10\n"; };$lastC=$c;next unless $. % 10 ==0;print "$start\t$depth\n" unless $depth<3' > $inputfilename".wig"
echo "wigToBigWig------"
wigToBigWig $inputfilename".wig" $chromsize $outputpath$inputfilename".bw"

rm $inputfilename".wig"
rm $inputfilename"_sorted.bam"


echo "end	" `date +%Y-%m-%d\ %H:%M:%S`
echo "Game over"
# example:
# bash bamtobw_zp.sh -i seq -o zp/ -c hg19.chrom.sizes 


