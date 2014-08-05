#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

engine = create_engine('sqlite:///topaz.db')
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

class Cycle(DeclarativeBase):
    __tablename__ = 'cycle'

    __table_args__ = {}

    #column definitions
    CYCLENUM = Column('CYCLENUM', INTEGER())
    DUTID = Column('DUTID', INTEGER(), ForeignKey('dut.ID'))
    ID = Column('ID', INTEGER(), primary_key=True, nullable=False)
    PGEMSTAT = Column('PGEMSTAT', INTEGER())
    READINESS = Column('READINESS', INTEGER())
    RESERVED = Column('RESERVED', INTEGER())
    TEMP = Column('TEMP', INTEGER())
    TIME = Column('TIME', INTEGER())
    VC1 = Column('VC1', INTEGER())
    VC2 = Column('VC2', INTEGER())
    VC3 = Column('VC3', INTEGER())
    VC4 = Column('VC4', INTEGER())
    VC5 = Column('VC5', INTEGER())
    VC6 = Column('VC6', INTEGER())
    VCAP = Column('VCAP', INTEGER())
    VIN = Column('VIN', INTEGER())

    #relation definitions


class Dut(DeclarativeBase):
    __tablename__ = 'dut'

    __table_args__ = {}

    #column definitions
    ARCHIEVED = Column('ARCHIEVED', INTEGER())
    CAPPN = Column('CAPPN', VARCHAR(length=10))
    CINT = Column('CINT', INTEGER())
    ENDUSR = Column('ENDUSR', VARCHAR(length=10))
    FWVER = Column('FWVER', VARCHAR(length=10))
    HWVER = Column('HWVER', VARCHAR(length=10))
    ID = Column('ID', INTEGER(), primary_key=True, nullable=False)
    LASTCAP = Column('LASTCAP', INTEGER())
    MESSAGE = Column('MESSAGE', VARCHAR(length=20))
    MFDATE = Column('MFDATE', VARCHAR(length=10))
    MODEL = Column('MODEL', VARCHAR(length=10))
    PCA = Column('PCA', VARCHAR(length=10))
    PCBVER = Column('PCBVER', VARCHAR(length=10))
    PWRCYCS = Column('PWRCYCS', INTEGER())
    SLOTNUM = Column('SLOTNUM', INTEGER())
    SN = Column('SN', VARCHAR(length=10))
    STATUS = Column('STATUS', INTEGER())
    TESTDATE = Column('TESTDATE', DATETIME())

    #relation definitions

