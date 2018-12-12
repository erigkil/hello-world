
#removes low quality scores in bam files below 12

import argparse,pysam,re,sys

def FilterReads(in_file, out_file):

    def read_ok(read):
          """
          read_ok - reject reads with a low quality (<12) base call
          read - a PySam AlignedRead object
          returns: True if the read is ok
          """
          if any([ord(c)-33 < _BASE_QUAL_CUTOFF for c in list(read.qual)]):
                 return False
          else:
                return True

_BASE_QUAL_CUTOFF = 12

bam_in = pysam.Samfile(in_file, 'rb')
bam_out = pysam.Samfile(out_file, 'wb', template=bam_in)

out_count = 0
for read in bam_in.fetch():
    if read_ok(read):
        bam_out.write(read)
        out_count += 1

print 'reads_written =', out_count

bam_out.close()
bam_in.close()


def GetArgs():
"""
GetArgs - read the command line
returns - an input bam file name and the output filtered bam file
"""

def ParseArgs(parser):
    class Parser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = Parser(description='Calculate PhiX Context Specific Error Rates.')
    parser.add_argument('-b', '--bam_file',
                        type=str,
                        required=True,
                        help='Input Bam file.')
    parser.add_argument('-o', '--output_file',
                        type=str,
                        required=True,
                        help='Output Bam file.')
    return parser.parse_args()

parser = argparse.ArgumentParser()
args = ParseArgs(parser)

return args.bam_file, args.output_file


def Main():
        bam_file, output_file = GetArgs()
FilterReads(bam_file, output_file)

 if __name__ == '__main__':
       Main()
	   
	   
	   
