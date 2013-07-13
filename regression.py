import sys
import multiprocess
import unittest
import nose
import os

class TestHWSWAdd(unittest.TestCase):
    """ test HW SW add func """

    def setUp(self):
        pass

    def teardown(self):
        os.system('rm -rf *.vpi')
        os.system('rm -rf *.vvp')
        os.system('rm -rf *.o')

    def buildup_vpi_db(vpi):
        """ build up vpi db called *.vpi ex: iverilog-vpi test.c """

        proc = subprocess.Popen("iverilog-vpi %s" %(vpi), \
                     shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()

    def buildup_v_db(tsuite, vpp, vlist=[]):
        """ build up verilog db called *.vvp ex: iverilog -otest.vpp test.v """

        proc = subprocess.Popen("iverilog -s %s -o%s %s" %(tsuite, vpp, " ".join(vlist)), \
                shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()

    def run_v_vpi_db(m, vpp):
        """ run sim by verilog and vpi db """

        proc = subprocess.Popen("vvp -M. -m%s %s" %(m, vpp), \
                shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()

    def test_add_over_flow(self):
        """ test add overfloat carry out, ..."""

    def test_add_normal(self):
        """ test add normal case """


if __name__ == '__main__':
    # call back by pydb debug when the exception happened
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb','--pdb-failure'], exit=False)
