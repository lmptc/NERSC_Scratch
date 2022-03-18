import os
import numpy as np
import time
from scipy import interpolate
import pickle
import sys

_,a,b,c,d,e = sys.argv

a,b,c,d = int(a), int(b), int(c), int(d)

# Path0 = '/global/homes/l/lianming/Presto-Color-2/data'
Path1 = '/global/cscratch1/sd/lianming/data/2Day_Interp'
# Path2 = '/global/homes/l/lianming/Presto-Color-2/data/2Day_Interp'

PathInterp = Path1

####### Parameter setting

EventNames = ['AGN', 'CART', 'EB', 'ILOT', 'MIRA', 'Mdwarf',
              'PISN', 'RRL', 'SLSN-I', 'SNII-NMF', 'SNII-Templates', 'SNIIn',
              'SNIa-91bg', 'SNIa-SALT2', 'SNIax', 'SNIbc-MOSFIT',
              'SNIbc-Templates', 'TDE', 'V19_CC+HostXT', 'uLens-Binary',
              'uLens-Single-GenLens', 'uLens-Single_PyLIMA']
EventNames = EventNames[a:b]

PointsPerDay = 0.1
ObjNo = 1000

#Coordinates

InfoDict = {}
InfoDict['EventNames'] = EventNames
InfoDict['PointsPerDay'] = PointsPerDay
InfoDict['Object Number'] = ObjNo

# InfoDict['Bands'] = ['u', 'g', 'r', 'i', 'z', 'Y']
InfoDict['Bands'] = list(e)
# InfoDict['dT1s'] = np.arange(0, 481, 15)
# InfoDict['dT2s'] =  np.arange(1, 481, 30)
InfoDict['dT1s'] = np.arange(c, d, 15)
InfoDict['dT2s'] =  np.arange(450, 451, 15)

InfoDict['BinMag'] = np.arange(-2.25, 4.06, 0.1)
InfoDict['BinColor'] = np.arange(-9.25, 9.8, 0.5)

HashTable = np.zeros([len(InfoDict['Bands']), len(InfoDict['Bands']), 
                      len(InfoDict['dT1s']), len(InfoDict['dT2s']), 
                      len(InfoDict['BinMag'])-1, len(InfoDict['BinColor'])-1], 
                     dtype='int32')

########
time1 = time.time()

dMagRange = [[], []]
ColorRange = [[], []]

for EventName in EventNames:
    
    print('##########################')
    print('This is the calculation of {}'.format(EventName))
    
    FilePath = os.path.join(PathInterp, EventName+'_Interp.pkl')
    with open(FilePath, 'rb') as f:
        Interp_load = pickle.load(f)
        TimeRange_load = pickle.load(f)  

    for ii, Band1 in enumerate(InfoDict['Bands']):
        for jj, Band2 in enumerate(InfoDict['Bands']):
            if jj==ii:
                continue
                
            print('Calculating bands {}{}'.format(Band1, Band2), end='\t')
               
            for kk, dT1 in enumerate(InfoDict['dT1s']):
                for ll, dT2 in enumerate(InfoDict['dT2s']):

                    dMag = []
                    Color = []

                    Thrs = {'u': 23.9, 'g': 25.0, 'r': 24.7, 'i': 24.0, 'z': 23.3, 'Y': 22.1}

                    if ObjNo == None:
                        ObjNo = len(Interp_load[Band1])

                    for II in range(ObjNo):

                        if Interp_load[Band1][II]==[] or Interp_load[Band2][II]==[]:
                            continuBe

                        TimeRangeStart = max( TimeRange_load[Band1][II][0], TimeRange_load[Band2][II][0] - dT1/1440 )
                        TimeRangeEnd = min( TimeRange_load[Band1][II][1] - dT2/1440, TimeRange_load[Band2][II][1] - dT1/1440 )

                        TimeRange = TimeRangeEnd - TimeRangeStart
                        SampleNo = int(PointsPerDay*TimeRange)

                        XX = np.random.rand(SampleNo)*TimeRange + TimeRangeStart

                        Mag1 = Interp_load[Band1][II](XX)
                        Mag2 = Interp_load[Band2][II](XX+dT1/1440)
                        Mag12 = Interp_load[Band1][II](XX+dT2/1440)

                        Mask = (Mag1<Thrs[Band1]) * (Mag2<Thrs[Band2]) *(Mag12<Thrs[Band1])

                        dMag.extend(Mag1[Mask] - Mag12[Mask])
                        Color.extend(Mag1[Mask] - Mag2[Mask])

                    data = np.array([dMag, Color])                        

                    histdata,_,_ = np.histogram2d(data[0], data[1], bins=[InfoDict['BinMag'], InfoDict['BinColor']])

                    dMagRange[0].append(data[0].min())
                    dMagRange[1].append(data[0].max())
                    ColorRange[0].append(data[1].min())
                    ColorRange[1].append(data[1].max())

                    outliersNo = len(data[0]) - np.sum(histdata)
                    if outliersNo != 0:
                        print('{:.0f} outliers found!'.format(outliersNo), end='')

#                         HashTable[ii, jj, kk, ll] = histdata*RateDict[EventName] + HashTable[ii, jj, kk, ll]
                    HashTable[ii, jj, kk, ll] = histdata + HashTable[ii, jj, kk, ll]

                print('|', end='')
                    
            print('')
            
print('Finish!')

print( '{} min spent.'.format( (time.time() - time1)/60 ))

############
# FolderPath = '/global/cscratch1/sd/lianming/Results'

# timestring = time.ctime()
# Len = len(EventNames)
# FileName = '_'.join(['ProbabilityCube', timestring[4:7]+timestring[8:10], timestring[11:16],
#                      ','.join( [ EventNames[ii] for ii in range(Len) if ii <3 ] + ['and_{}_more'.format(Len-3) for _ in range(1) if Len>3]  ) ] )

# FilePath = os.path.join(FolderPath, FileName+'.pkl')
# FilePath0 = FilePath

# ii = 1
# while os.path.exists(FilePath):
#     FilePath = FilePath0[:-4] + '('+str(ii)+')' + '.pkl'
#     ii += 1

# with open(FilePath, 'wb') as f:
#     pickle.dump(EventNames, f)
#     pickle.dump(InfoDict, f)
#     pickle.dump(HashTable, f ) 