from sqlalchemy.sql.expression import delete
from sqlalchemy import create_engine, insert, delete, update
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#mysql+mysqlconnector://root:Mysqlbase103@localhost:3306/rentalfilm
engine = create_engine('mysql+mysqlconnector://root:admin@localhost:3306/DoraemonDB', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

meta = MetaData()

# Create tables
dorayaki = Table(
    'dorayaki', meta, 
    Column('id', Integer, primary_key = True), 
    Column('rasa', String(50)), 
    Column('deskripsi', String(255)), 
    Column('gambar', LargeBinary)
)

store = Table(
    'store', meta,
    Column('id', Integer, primary_key = True), 
    Column('nama', String(50)), 
    Column('jalan', String(255)), 
    Column('kecamatan', String(255)),
    Column('provinsi', String(255))
)

store_items = Table(
    'store_items', meta,
    Column('store_id', Integer, ForeignKey('store.id'), primary_key=True),
    Column('dorayaki_id', Integer, ForeignKey('dorayaki.id'), primary_key=True),
    Column('jumlah_stok', Integer)
)

meta.create_all(engine)

class Dorayaki(Base):
   __tablename__ = 'dorayaki'
   id = Column(Integer, primary_key = True, autoincrement=True)
   rasa = Column(String)
   deskripsi = Column(String)
   gambar = Column(LargeBinary)

class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key = True, autoincrement=True)
    nama = Column(String)
    jalan = Column(String)
    kecamatan = Column(String)
    provinsi = Column(String)

class StoreItem(Base):
    __tablename__ = 'store_items'
    store_id = Column(Integer, primary_key = True, autoincrement=True)
    dorayaki_id = Column(Integer, primary_key = True, autoincrement=True)
    jumlah_stok = Column(Integer)

# Data Seeding
# Load images
images = [bytes(imageBinary, 'utf-8') for imageBinary in open("models/dora_images.txt", "r").read().split(",")]

if (len(session.query(Dorayaki).all()) == 0):
    initDora1 = Dorayaki(
        id = 1,
        rasa = "Coklat",
        deskripsi = "Ketika disantap, dorayaki akan terasa manis dan lembut sehingga membuat siapapun yang mencobanya jadi ketagihan.",
        gambar = images[0]
    )

    initDora2 = Dorayaki(
        id = 2,
        rasa = "Keju",
        deskripsi = "Kue dorayaki keju adalah sajian yang lezat untuk disantap.",
        gambar = images[1]
    )

    initDora3 = Dorayaki(
        id = 3,
        rasa = "Red Velvet",
        deskripsi = "Yang satu ini beda dengan dorayaki biasa karena berwarna merah dengan rasa red velvet!",
        gambar = images[2]
    )

    session.add_all([initDora1, initDora2, initDora3])
    session.commit()

if (len(session.query(Store).all()) == 0):
    initStore1 = Store (
        id = 1,
        nama = "Toko Sejahtera Utama",
        jalan = "Jl. Lap. Roos Kali",
        kecamatan = "Menteng",
        provinsi = "DKI Jakarta"
    )

    initStore2 = Store (
        id = 2,
        nama = "Toko Rahmat Sentosa",
        jalan = "Jl. Batam",
        kecamatan = "Serpong",
        provinsi = "Banten"
    )

    initStore3 = Store (
        id = 3,
        nama = "Toko Indonesia Jaya",
        jalan = "4 Jl. Dahlia",
        kecamatan = "Samarinda",
        provinsi = "Kalimantan Timur"
    )
    
    session.add_all([initStore1, initStore2, initStore3])
    session.commit()

if (len(session.query(StoreItem).all()) == 0):
    initStoreItem1 = StoreItem (
        store_id = 1,
        dorayaki_id = 1,
        jumlah_stok = 2
    )

    initStoreItem2 = StoreItem (
        store_id = 2,
        dorayaki_id = 1,
        jumlah_stok = 3
    )

    initStoreItem3 = StoreItem (
        store_id = 2,
        dorayaki_id = 2,
        jumlah_stok = 10
    )

    initStoreItem4 = StoreItem (
        store_id = 1,
        dorayaki_id = 3,
        jumlah_stok = 1
    )

    initStoreItem5 = StoreItem (
        store_id = 3,
        dorayaki_id = 2,
        jumlah_stok = 9
    )

    initStoreItem6 = StoreItem (
        store_id = 3,
        dorayaki_id = 3,
        jumlah_stok = 5
    )

    session.add_all([initStoreItem1, initStoreItem2, initStoreItem3, initStoreItem4, initStoreItem5, initStoreItem6])
    session.commit()