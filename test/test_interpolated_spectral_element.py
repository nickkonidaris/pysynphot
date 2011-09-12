from __future__ import division

import os.path

import numpy as np

import nose.tools

import testutil

import pysynphot as S
from pysynphot import observationmode
import pysynphot.exceptions as exceptions

# test whether the InterpolatedSpectralElement grabs the correct column
# when the input value is a column (no interpolation required) and an "ERROR"
# column is present
class InterpErrorColCase(testutil.FPTestCase):
  def setUp(self):
    interp_val = 51252.0
    filename = os.path.join('comp','stis','stis_nm16_mjd_010_syn.fits')
    filename = S.observationmode._refTable(filename) + '[MJD#]'
    self.spec = S.spectrum.InterpolatedSpectralElement(filename,interp_val)
    
  def test_throughput(self):
    throughput = \
      np.array([ 0.      ,  0.965065,  0.965065,  0.965065,  0.963328,  0.976245,
                  0.983497,  0.984206,  0.976436,  0.963131,  0.950973,  0.952877,
                  0.951205,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,  0.980966,
                  0.980966,  0.980966,  0.980966,  0.      ])
    
    self.assertEqualNumpy(self.spec._throughputtable,throughput)
    
  def test_wavetable(self):
    wavetable = \
      np.array([  1049.,   1050.,   1100.,   1150.,   1200.,   1250.,   1300.,
         1350.,   1400.,   1450.,   1500.,   1550.,   1600.,   1650.,
         1700.,   1750.,   1800.,   1850.,   1900.,   1950.,   2000.,
         2050.,   2100.,   2150.,   2200.,   2250.,   2300.,   2350.,
         2400.,   2450.,   2500.,   2550.,   2600.,   2650.,   2700.,
         2750.,   2800.,   2850.,   2900.,   2950.,   3000.,   3050.,
         3100.,   3150.,   3200.,   3250.,   3300.,   3350.,   3400.,
         3450.,   3500.,   3550.,   3600.,   3650.,   3700.,   3750.,
         3800.,   3850.,   3900.,   3950.,   4000.,   4050.,   4100.,
         4150.,   4200.,   4250.,   4300.,   4350.,   4400.,   4450.,
         4500.,   4550.,   4600.,   4650.,   4700.,   4750.,   4800.,
         4850.,   4900.,   4950.,   5000.,   5050.,   5100.,   5150.,
         5200.,   5250.,   5300.,   5350.,   5400.,   5450.,   5500.,
         5550.,   5600.,   5650.,   5700.,   5750.,   5800.,   5850.,
         5900.,   5950.,   6000.,   6050.,   6100.,   6150.,   6200.,
         6250.,   6300.,   6350.,   6400.,   6450.,   6500.,   6550.,
         6600.,   6650.,   6700.,   6750.,   6800.,   6850.,   6900.,
         6950.,   7000.,   7050.,   7100.,   7150.,   7200.,   7250.,
         7300.,   7350.,   7400.,   7450.,   7500.,   7550.,   7600.,
         7650.,   7700.,   7750.,   7800.,   7850.,   7900.,   7950.,
         8000.,   8050.,   8100.,   8150.,   8200.,   8250.,   8300.,
         8350.,   8400.,   8450.,   8500.,   8550.,   8600.,   8650.,
         8700.,   8750.,   8800.,   8850.,   8900.,   8950.,   9000.,
         9050.,   9100.,   9150.,   9200.,   9250.,   9300.,   9350.,
         9400.,   9450.,   9500.,   9550.,   9600.,   9650.,   9700.,
         9750.,   9800.,   9850.,   9900.,   9950.,  10000.,  10050.,
        10100.,  10150.,  10200.,  10250.,  10300.,  10350.,  10400.,
        10450.,  10500.,  10550.,  10600.,  10650.,  10700.,  10750.,
        10800.,  10850.,  10900.,  10950.,  11000.,  11001.])
        
    self.assertEqualNumpy(self.spec._wavetable,wavetable)

# test whether the InterpolatedSpectralElement grabs the correct column
# when the input value is the first column (no interpolation required) and 
# there is no "throughput" (default) column present, meaning that the 
# interpolation columns start at column 1
class InterpNoDefaultCase(testutil.FPTestCase):
  def setUp(self):
    interp_val = 0.0
    filename = os.path.join('comp','acs','acs_wfc_aper_002_syn.fits')
    filename = S.observationmode._refTable(filename) + '[aper#]'
    self.spec = S.spectrum.InterpolatedSpectralElement(filename,interp_val)
    
  def test_throughput(self):
    throughput = \
      np.array([ 0.28      ,  0.22      ,  0.20999999,  0.22      ,  0.22      ,
        0.2       ,  0.15000001,  0.1       ,  0.04      ], dtype=np.float32)
    
    self.assertEqualNumpy(self.spec._throughputtable,throughput)
    
  def test_wavetable(self):
    wavetable = \
      np.array([  3500.,   4000.,   5000.,   6000.,   7000.,   8000.,   9000.,
        10000.,  11000.], dtype=np.float32)
        
    self.assertEqualNumpy(self.spec._wavetable,wavetable)
    
# test whether the InterpolatedSpectralElement gets the correct throughput table
# in the event that it is passed a value that does not correspond to a column
# and interpolation is required.
class InterpInterpolationRequiredCase(testutil.FPTestCase):
  def setUp(self):
    interp_val = 51000.0
    filename = os.path.join('comp','stis','stis_nm16_mjd_010_syn.fits')
    filename = S.observationmode._refTable(filename) + '[MJD#]'
    self.spec = S.spectrum.InterpolatedSpectralElement(filename,interp_val)
    
  def test_throughput(self):
    throughput = \
      np.array([ 0.        ,  0.97830353,  0.97830353,  0.97830353,  0.97722476,
        0.98524689,  0.98975077,  0.99019109,  0.98536552,  0.97710241,
        0.96955165,  0.97073414,  0.96969574,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.98817888,  0.98817888,  0.98817888,  0.98817888,
        0.98817888,  0.        ])
    
    self.assertEqual(self.spec._throughputtable[0],throughput[0])
    self.assertEqual(self.spec._throughputtable[-1],throughput[-1])
    self.assertApproxNumpy(self.spec._throughputtable[1:-1],throughput[1:-1])
    
  def test_wavetable(self):
    wavetable = \
      np.array([  1049.,   1050.,   1100.,   1150.,   1200.,   1250.,   1300.,
         1350.,   1400.,   1450.,   1500.,   1550.,   1600.,   1650.,
         1700.,   1750.,   1800.,   1850.,   1900.,   1950.,   2000.,
         2050.,   2100.,   2150.,   2200.,   2250.,   2300.,   2350.,
         2400.,   2450.,   2500.,   2550.,   2600.,   2650.,   2700.,
         2750.,   2800.,   2850.,   2900.,   2950.,   3000.,   3050.,
         3100.,   3150.,   3200.,   3250.,   3300.,   3350.,   3400.,
         3450.,   3500.,   3550.,   3600.,   3650.,   3700.,   3750.,
         3800.,   3850.,   3900.,   3950.,   4000.,   4050.,   4100.,
         4150.,   4200.,   4250.,   4300.,   4350.,   4400.,   4450.,
         4500.,   4550.,   4600.,   4650.,   4700.,   4750.,   4800.,
         4850.,   4900.,   4950.,   5000.,   5050.,   5100.,   5150.,
         5200.,   5250.,   5300.,   5350.,   5400.,   5450.,   5500.,
         5550.,   5600.,   5650.,   5700.,   5750.,   5800.,   5850.,
         5900.,   5950.,   6000.,   6050.,   6100.,   6150.,   6200.,
         6250.,   6300.,   6350.,   6400.,   6450.,   6500.,   6550.,
         6600.,   6650.,   6700.,   6750.,   6800.,   6850.,   6900.,
         6950.,   7000.,   7050.,   7100.,   7150.,   7200.,   7250.,
         7300.,   7350.,   7400.,   7450.,   7500.,   7550.,   7600.,
         7650.,   7700.,   7750.,   7800.,   7850.,   7900.,   7950.,
         8000.,   8050.,   8100.,   8150.,   8200.,   8250.,   8300.,
         8350.,   8400.,   8450.,   8500.,   8550.,   8600.,   8650.,
         8700.,   8750.,   8800.,   8850.,   8900.,   8950.,   9000.,
         9050.,   9100.,   9150.,   9200.,   9250.,   9300.,   9350.,
         9400.,   9450.,   9500.,   9550.,   9600.,   9650.,   9700.,
         9750.,   9800.,   9850.,   9900.,   9950.,  10000.,  10050.,
        10100.,  10150.,  10200.,  10250.,  10300.,  10350.,  10400.,
        10450.,  10500.,  10550.,  10600.,  10650.,  10700.,  10750.,
        10800.,  10850.,  10900.,  10950.,  11000.,  11001.])
        
    self.assertEqualNumpy(self.spec._wavetable,wavetable)


# test that an exception is raised when we can't extrapolate
# and there's no default
def aper_no_extrap_test():
  interp_val = -5.
  filename = os.path.join('comp','acs','acs_wfc_aper_002_syn.fits')
  filename = S.observationmode._refTable(filename) + '[aper#]'
  
  nose.tools.assert_raises(exceptions.ExtrapolationNotAllowed,
                            S.spectrum.InterpolatedSpectralElement,
                            filename,interp_val)


class RampFilterTest(testutil.FPTestCase):
  def setUp(self):
    interp_val = 6480.
    filename = os.path.join('comp','acs','acs_fr656n_005_syn.fits')
    filename = S.observationmode._refTable(filename) + '[fr656n#]'
    self.spec = S.spectrum.InterpolatedSpectralElement(filename,interp_val)
    
  def test_throughput(self):
    throughput = \
      np.array([  5.88854514e-07,   5.88854514e-07,   1.00092827e-06,
         1.00095364e-06,   1.00098034e-06,   1.00100847e-06,
         1.00103817e-06,   1.00106947e-06,   1.00110253e-06,
         1.00114265e-06,   1.00120149e-06,   1.00126380e-06,
         1.00132978e-06,   1.00139959e-06,   1.00147357e-06,
         1.00155197e-06,   1.00163515e-06,   1.00172337e-06,
         1.00181695e-06,   1.00191626e-06,   1.00202179e-06,
         1.00213390e-06,   1.00225310e-06,   1.00237987e-06,
         1.00251477e-06,   1.00265846e-06,   1.00281167e-06,
         1.00297512e-06,   1.00314982e-06,   1.00333682e-06,
         1.00353753e-06,   1.00375356e-06,   1.00398704e-06,
         1.00424066e-06,   1.00451809e-06,   1.00482407e-06,
         1.00516509e-06,   1.00554984e-06,   1.00599029e-06,
         1.00650247e-06,   1.00710832e-06,   1.00783727e-06,
         1.00872907e-06,   1.00983676e-06,   1.01123096e-06,
         1.01300472e-06,   1.01528024e-06,   1.01821653e-06,
         1.02201921e-06,   1.02695196e-06,   1.03335088e-06,
         1.04164075e-06,   1.05235463e-06,   1.06615679e-06,
         1.08386847e-06,   1.10649810e-06,   1.13527471e-06,
         1.17168563e-06,   1.21751801e-06,   1.27490410e-06,
         1.34637005e-06,   1.43488805e-06,   1.54393129e-06,
         1.67753038e-06,   1.84033133e-06,   2.03765491e-06,
         2.27555160e-06,   2.56085724e-06,   2.90124536e-06,
         3.30526926e-06,   3.78240595e-06,   4.34308278e-06,
         4.99869611e-06,   5.76162707e-06,   6.64522621e-06,
         7.66379784e-06,   8.83257842e-06,   1.01676570e-05,
         1.16859276e-05,   1.34050020e-05,   1.53430929e-05,
         1.75188984e-05,   1.99514691e-05,   2.26600455e-05,
         2.56638970e-05,   2.89821330e-05,   3.26335264e-05,
         3.66363154e-05,   4.10079861e-05,   4.57650824e-05,
         5.09230156e-05,   5.64958366e-05,   6.24960682e-05,
         6.89345517e-05,   7.58202527e-05,   8.31601110e-05,
         9.09589531e-05,   9.92193733e-05,   1.07941705e-04,
         1.17123904e-04])
        
    self.assertApproxNumpy(self.spec._throughputtable[:100],throughput)
    
  def test_wavetable(self):
    wavetable = \
      np.array([ 3499.99902344,  3500.        ,  5646.        ,  5651.        ,
        5656.        ,  5661.        ,  5666.        ,  5671.        ,
        5676.        ,  5681.        ,  5686.        ,  5691.        ,
        5696.        ,  5701.        ,  5706.        ,  5711.        ,
        5716.        ,  5721.        ,  5726.        ,  5731.        ,
        5736.        ,  5741.        ,  5746.        ,  5751.        ,
        5756.        ,  5761.        ,  5766.        ,  5771.        ,
        5776.        ,  5781.        ,  5786.        ,  5791.        ,
        5796.        ,  5801.        ,  5806.        ,  5811.        ,
        5816.        ,  5821.        ,  5826.        ,  5831.        ,
        5836.        ,  5841.        ,  5846.        ,  5851.        ,
        5856.        ,  5861.        ,  5866.        ,  5871.        ,
        5876.        ,  5881.        ,  5886.        ,  5891.        ,
        5896.        ,  5901.        ,  5906.        ,  5911.        ,
        5916.        ,  5921.        ,  5926.        ,  5931.        ,
        5936.        ,  5941.        ,  5946.        ,  5951.        ,
        5956.        ,  5961.        ,  5966.        ,  5971.        ,
        5976.        ,  5981.        ,  5986.        ,  5991.        ,
        5996.        ,  6001.        ,  6006.        ,  6011.        ,
        6016.        ,  6021.        ,  6026.        ,  6031.        ,
        6036.        ,  6041.        ,  6046.        ,  6051.        ,
        6056.        ,  6061.        ,  6066.        ,  6071.        ,
        6076.        ,  6081.        ,  6086.        ,  6091.        ,
        6096.        ,  6101.        ,  6106.        ,  6111.        ,
        6116.        ,  6121.        ,  6126.        ,  6131.        ])
        
    self.assertApproxNumpy(self.spec._wavetable[:100],wavetable)


class RampFilterExtrapTest(RampFilterTest):
  def setUp(self):
    interp_val = -5.
    filename = os.path.join('comp','acs','acs_fr656n_005_syn.fits')
    filename = S.observationmode._refTable(filename) + '[fr656n#]'
    self.spec = S.spectrum.InterpolatedSpectralElement(filename,interp_val)
    
  def test_throughput(self):
    self.assertTrue((self.spec._throughputtable == 0).all())
    
  def test_warnings(self):
    assert self.spec.warnings['DefaultThroughput'] is True
    

# this is here because WFPC2 CONT# tables have both CONT# and ERR# columns
# and both were being grabbed and used by InterpolatedSpectralElement.
# This tests my fix.
class TestWFPC2Cont(testutil.FPTestCase):
  def test_wfpc2_cont(self):
    bp = S.ObsBandpass('wfpc2,1,a2d7,f300w,cont#49892.0')
    ur = bp.unit_response()
    
    self.assertApproxFP(ur,6.3011E-17,accuracy=1.e-4)
