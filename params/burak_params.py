import pandas as pd

param_names = ['IMU', 'GPS', 'GPA', 'MAG', 'ARSP', 'RCOU', 'BARO', 'ESC',
               'PIDR', 'PIDP', 'PIDY', 'PIDA', 'PIDS', 'PIDN', 'PIDE',
               'ACC', 'GYR', 'ATT', 'ORGN', 'RATE', 'VSTB', 'MON', 'PSCN',
               'PSCE', 'PSCD', 'CTUN', 'NTUN', 'ATRP', 'STAT', 'CMDI']


class IMUParser:

    def __init__(self):
        self.label = 'IMU'
        self.description = 'Inertial Measurement Unit data'
        self.TimeUS = []
        self.I = []
        self.GyrX = []
        self.GyrY = []
        self.GyrZ = []
        self.AccX = []
        self.AccY = []
        self.AccZ = []
        self.T = []
        self.GH = []
        self.AH = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 16:
            return
        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.GyrX.append(float(line[3]))
        self.GyrY.append(float(line[4]))
        self.GyrZ.append(float(line[5]))
        self.AccX.append(float(line[6]))
        self.AccY.append(float(line[7]))
        self.AccZ.append(float(line[8]))
        self.T.append(float(line[11]))
        self.GH.append(int(line[12]))
        self.AH.append(int(line[13]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'GyrX': self.GyrX,
                'GyrY': self.GyrY,
                'GyrZ': self.GyrZ,
                'AccX': self.AccX,
                'AccY': self.AccY,
                'AccZ': self.AccZ,
                'T': self.T,
                'GH': self.GH,
                'AH': self.AH,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class GPSParser:
    def __init__(self):
        self.label = 'GPS'
        self.TimeUS = []
        self.I = []
        self.Status = []
        self.NSats = []
        self.HDop = []
        self.Lat = []
        self.Lng = []
        self.Alt = []
        self.Spd = []
        self.GCrs = []
        self.VZ = []
        self.Yaw = []

    def update(self, line):
        line = line.split(',')
# GPS, 358913592, 0, 3, 467933800, 2219, 8, 1.77, 39.9639066, 32.8967033, 953.63, 0.116, 237.9506, 0.044, 0, 1

        # error checking
        if len(line) < 16:
            return
        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.Status.append(float(line[3]))
        self.NSats.append(float(line[6]))
        self.HDop.append(float(line[7]))
        self.Lat.append(float(line[8]))
        self.Lng.append(float(line[9]))
        self.Alt.append(float(line[10]))
        self.Spd.append(float(line[11]))
        self.GCrs.append(float(line[12]))
        self.VZ.append(float(line[13]))
        self.Yaw.append(float(line[14]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'Status': self.Status,
                'NSats': self.NSats,
                'HDop': self.HDop,
                'Lat': self.Lat,
                'Lng': self.Lng,
                'Alt': self.Alt,
                'Spd': self.Spd,
                'GCrs': self.GCrs,
                'VZ': self.VZ,
                'Yaw': self.Yaw,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class GPAParser:
    def __init__(self):
        self.label = 'GPA'
        self.TimeUS = []
        self.I = []
        self.VDop = []
        self.HAcc = []
        self.VAcc = []
        self.SAcc = []
        self.YAcc = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 11:
            return
        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.VDop.append(float(line[3]))
        self.HAcc.append(float(line[4]))
        self.VAcc.append(float(line[5]))
        self.SAcc.append(float(line[6]))
        self.YAcc.append(float(line[7]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'VDop': self.VDop,
                'HAcc': self.HAcc,
                'VAcc': self.VAcc,
                'SAcc': self.SAcc,
                'YAcc': self.YAcc,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class MAGParser:
    def __init__(self):
        self.label = 'MAG'
        self.TimeUS = []
        self.I = []
        self.MagX = []
        self.MagY = []
        self.MagZ = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 11:
            return
        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.MagX.append(float(line[3]))
        self.MagY.append(float(line[4]))
        self.MagZ.append(float(line[5]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'MagX': self.MagX,
                'MagY': self.MagY,
                'MagZ': self.MagZ,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class ARSPParser:
    def __init__(self):
        self.label = 'ARSP'
        self.TimeUS = []
        self.I = []
        self.AirSpeed = []
        self.DiffPress = []
        self.Temp = []
        self.RawPress = []
        self.U = [] # true if the sensor is being used
        self.H = [] # true if the sensor is healthy

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 12:
            return

        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.AirSpeed.append(float(line[3]))
        self.DiffPress.append(float(line[4]))
        self.Temp.append(float(line[5]))
        self.RawPress.append(float(line[6]))
        self.U.append(int(line[8]))
        self.H.append(int(line[9]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'AirSpeed': self.AirSpeed,
                'DiffPress': self.DiffPress,
                'Temp': self.Temp,
                'RawPress': self.RawPress,
                'U': self.U,
                'H': self.H,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class RCOUParser:
    def __init__(self):
        self.label = 'RCOU'
        self.TimeUS = []
        self.C1 = []
        self.C2 = []
        self.C3 = []
        self.C4 = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 16:
            return

        self.TimeUS.append(int(line[1]))
        self.C1.append(int(line[2]))
        self.C2.append(float(line[3]))
        self.C3.append(float(line[4]))
        self.C4.append(float(line[5]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'C1': self.C1,
                'C2': self.C2,
                'C3': self.C3,
                'C4': self.C4,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class BAROParser:
    def __init__(self):
        self.label = 'BARO'
        self.TimeUS = []
        self.I = []
        self.Alt = []
        self.Press = []
        self.Temp = []
        self.CRt = []
        self.Health = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 11:
            return

        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.Alt.append(float(line[3]))
        self.Press.append(float(line[4]))
        self.Temp.append(float(line[5]))
        self.CRt.append(float(line[5]))
        self.Health.append(float(line[10]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'Alt': self.Alt,
                'Press': self.Press,
                'Temp': self.Temp,
                'CRt': self.CRt,
                'Health': self.Health,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class ESCParser:
    def __init__(self):
        self.label = 'ESC'
        self.TimeUS = []
        self.I = []
        self.RPM = []
        self.RawRPM = []
        self.Volt = []
        self.Curr = []
        self.Temp = []
        self.CTot = []
        self.MotTemp = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 11:
            return

        self.TimeUS.append(int(line[1]))
        self.I.append(int(line[2]))
        self.RPM.append(float(line[3]))
        self.RawRPM.append(float(line[4]))
        self.Volt.append(float(line[5]))
        self.Curr.append(float(line[6]))
        self.Temp.append(float(line[7]))
        self.CTot.append(float(line[8]))
        self.MotTemp.append(float(line[9]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'I': self.I,
                'RPM': self.RPM,
                'RawRPM': self.RawRPM,
                'Volt': self.Volt,
                'Curr': self.Curr,
                'Temp': self.Temp,
                'CTot': self.CTot,
                'MotTemp': self.MotTemp,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


class PIDRParser:
    def __init__(self):
        self.label = 'PIDR'
        self.TimeUS = []
        self.Tar = []
        self.Act = []
        self.Err = []
        self.P = []
        self.I = []
        self.D = []

    def update(self, line):
        line = line.split(',')

        # error checking
        if len(line) < 12:
            return

        self.TimeUS.append(int(line[1]))
        self.Tar.append(float(line[2]))
        self.Act.append(float(line[3]))
        self.Err.append(float(line[4]))
        self.P.append(float(line[5]))
        self.I.append(float(line[6]))
        self.D.append(float(line[7]))

    def get_data_frame(self):
        temp = {'TimeUS': self.TimeUS,
                'Tar': self.Tar,
                'Act': self.Act,
                'Err': self.Err,
                'P': self.P,
                'I': self.I,
                'D': self.D,
                }
        df = pd.DataFrame.from_dict(temp)
        df.name = self.label
        return df


IMUParser = IMUParser()
PIDRParser = PIDRParser()
ESCParser = ESCParser()
BAROParser = BAROParser()
RCOUParser = RCOUParser()
ARSPParser = ARSPParser()
MAGParser = MAGParser()
GPAParser = GPAParser()
GPSParser = GPSParser()
