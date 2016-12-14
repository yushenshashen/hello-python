#!/bin/sh

##----INTRO-----------##
# Name=bam2bw.sh
# Date=Apr 25, 2016
# Update=
#-Kaili Fan-#

######
# Purpose
#This file is for turning bam file to bigwig.
#1 
#2

##----Start-----------##
echo "\033[31m  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@ \033[0m"
start=$(date +%Y-%m-%d\ %H:%M:%S)
echo "\033[31m BEGIN@ "$start" \033[0m"
echo "\033[31m  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@  @o@ \033[0m"

##----Arguments-------##
help_info(){
	echo "usage:"
	echo "sh bam2bw.sh <option>* [-i inputPath] [-f fileName] [-o outputPath] [-c chromSize] "
	echo ""
	echo "Arguments:"
	echo "-i The input_file path."
	echo "-f the fileName."
	echo "-o the output_file path."
	echo "-c the chromSize file."
	echo ""
	echo "This file process for turning bam file to bigwig."
	echo "All path should end with '/'."
	echo "All inputFile should be end with '.bam'."
	echo ""
}

if [ $# -lt 4 ];then
	help_info
	exit 1
fi

CPU=1

while getopts "i:f:o:c:" Arg
do
	case $Arg in
		i)	inputPath=$OPTARG;;
		f)	fileName=$OPTARG;;
		o)	outputPath=$OPTARG;;
		c)	chromSize=$OPTARG;;
		?)	echo "Wrong parameter!!!"
			exit 1;;
	esac
done


########################
cd ${inputPath}
# get name for naming outputFile
name=${fileName%.bam}
# sort file
samtools sort ${fileName} ${name}_sorted.bam
# bam2wig
samtools depth ${name}_sorted.bam | perl -ne 'BEGIN{ print "track type=print wiggle_0 name=fileName description=fileName\n"}; ($c, $start, $depth) = split;if ($c ne $lastC) { print "variableStep chrom=$c span=10\n"; };$lastC=$c;next unless $. % 10 ==0;print "$start\t$depth\n" unless $depth<3' > ${name}.wig
# wig2bw
wigToBigWig ${name}.wig ${chromSize} ${outputPath}${name}.bw
# remove intermediate result
rm ${name}_sorted.bam ${name}.wig


echo "Well done!"
echo "^_^"
echo "Finished!!!"
#########################
echo "\033[31m ^m^ ^m^  ^m^  ^m^  ^m^  ^m^ ^m^  ^m^  ^m^  ^m^ ^m^ ^m^  ^m^  ^m^  ^m^ ^m^ ^m^  ^m^  ^m^  ^m^ \033[0m"
end=$(date +%Y-%m-%d\ %H:%M:%S)
echo "\033[31m END@ "$end" \033[0m"
sTime=`date -d "$start" +%s` 
eTime=`date -d "$end" +%s`
interval=`expr $eTime - $sTime` 
echo "\033[31m This Program run for "$interval" seconds. \033[0m"
echo "\033[31m ^m^ ^m^  ^m^  ^m^  ^m^  ^m^ ^m^  ^m^  ^m^  ^m^ ^m^ ^m^  ^m^  ^m^  ^m^ ^m^ ^m^  ^m^  ^m^  ^m^ \033[0m"
