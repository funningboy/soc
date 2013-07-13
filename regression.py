# HW/SW regression flow by python nose unittest
# 1. using subprocess call third part system call
# 2. using regular expression to parse the log
# 3. register each testsuite to test Manager

import sys
import subprocess
import unittest
import nose
import os
import re

reERROR = re.compile(r"ERROR", re.M)


class TestHWSWAdd(unittest.TestCase):
    """ test HW SW add func """

    def setUp(self):
        pass

    def tearDown(self):
        """ purge all """

        os.system('rm -rf *.vpi')
        os.system('rm -rf *.vvp')
        os.system('rm -rf *.o')
        os.system('rm -rf *.log')


    def buildup_vpi_db(self, vpi):
        """ build up vpi db called *.vpi ex: iverilog-vpi test.c """

        proc = subprocess.Popen("iverilog-vpi %s" %(vpi), \
                     shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()


    def buildup_v_db(self, tsuite, vpp, vlist=[]):
        """ build up verilog db called *.vvp ex: iverilog -otest.vpp test.v """

        proc = subprocess.Popen("iverilog -s %s -o%s %s" %(tsuite, vpp, " ".join(vlist)), \
                shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()


    def run_v_vpi_db(self, m, vpp, log):
        """ run sim by verilog and vpi db """

        proc = subprocess.Popen("vvp -M. -m%s %s > %s" %(m, vpp, log), \
                shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        id(proc)
        proc.wait()


    def analysis_log(self, log):
        """ analysis the log is pass or fail """

        f = open(log, 'r')
        founds = reERROR.findall(f.read().replace('\n', ''))
        f.close()

        if founds:
            return False
        return True

    def test_add_over_float(self):
        """ test add overfloat carry out, ..."""

        self.buildup_vpi_db('./vpi/vpi_add.c')
        self.buildup_v_db('test_over_float', 'vpi_add.vvp', ['dut.v', './test/test_dut.v'])
        self.run_v_vpi_db('vpi_add', 'vpi_add.vvp', 'test_over_float.log')
        self.assertTrue(self.analysis_log('test_over_float.log'))


    def test_add_normal(self):
        """ test add normal case """

        self.buildup_vpi_db('./vpi/vpi_add.c')
        self.buildup_v_db('test_add_normal', 'vpi_add.vvp', ['dut.v', './test/test_dut.v'])
        self.run_v_vpi_db('vpi_add', 'vpi_add.vvp', 'test_add_normal.log')
        self.assertTrue(self.analysis_log('test_add_normal.log'))


if __name__ == '__main__':
    # call back by pydb debug when the exception happened
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb','--pdb-failure'], exit=False)
