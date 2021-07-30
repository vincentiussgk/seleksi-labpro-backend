from flask import Flask, jsonify, request
from models.models import Dorayaki, Store, StoreItem, session, dorayaki, store, store_items
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def your_root_route():
    return "hello"

#  Dorayaki Methods

def getDorayaki():
    allDorayaki = session.query(Dorayaki).all()
    jsonDorayaki = []
    for column in allDorayaki:
        jsonDorayaki.append({
            "id": column.id,
            "rasa": column.rasa,
            "deskripsi": column.deskripsi,
            "gambar": column.gambar.decode('ascii')
        })
    return jsonify(jsonDorayaki)
    
def addDorayaki():
    requestData = request.get_json()
    insertDorayaki = Dorayaki(
        id = requestData.get("id") or None,
        rasa = requestData["rasa"],
        deskripsi = requestData["deskripsi"],
        gambar = bytes(requestData["gambar"], 'utf-8')
    )
    session.add(insertDorayaki)
    try:
        session.commit()
        return "Post Success"
    except Exception as e:
        return e

def deleteDorayaki():
    requestData = request.get_json()
    doraId = requestData.get("id")
    session.query(Dorayaki).filter(Dorayaki.id == doraId).delete()
    try:
        session.commit()
        return "Delete Success"
    except Exception as e:
        return e

def updateDorayaki():
    requestData = request.get_json()
    doraId = requestData.get("id")
    result = session.query(Dorayaki).filter(Dorayaki.id == doraId).one()
    for key in requestData.keys():
        if (key != "id"):
            if (key == "gambar"):
                setattr(result, key, bytes(requestData[key], 'utf-8'))
            else:
                setattr(result, key, requestData[key])
    try:
        session.commit()
        return "Update Success"
    except Exception as e:
        return e
    

@app.route("/dorayaki", methods=["GET", "POST", "DELETE", "PUT"])
def accessDorayaki():
    if (request.method == "GET"):
        return getDorayaki()
    elif (request.method == "POST"):
        return addDorayaki()    
    elif (request.method == "DELETE"):
        return deleteDorayaki()
    elif (request.method == "PUT"):
        return updateDorayaki()

# ======== End dorayaki methods ===========
# Store Methods

def getStore():
    allStore = session.query(Store).all()
    jsonDorayaki = []
    for column in allStore:
        jsonDorayaki.append({
            "id": column.id,
            "nama": column.nama,
            "jalan": column.jalan,
            "kecamatan": column.kecamatan,
            "provinsi": column.provinsi
        })
    return jsonify(jsonDorayaki)
    
def addStore():
    requestData = request.get_json()
    insertStore = Store(
        id = requestData.get("id") or None,
        nama = requestData["nama"],
        jalan = requestData["jalan"],
        kecamatan = requestData["kecamatan"],
        provinsi = requestData["provinsi"],
    )
    session.add(insertStore)
    try:
        session.flush()
        newId = insertStore.id
        session.commit()
        return jsonify({ "id" : newId })
    except Exception as e:
        return e

def deleteStore():
    requestData = request.get_json()
    storeId = requestData.get("id")
    session.query(Store).filter(Store.id == storeId).delete()
    try:
        session.commit()
        return "Delete Success"
    except Exception as e:
        return e

def updateStore():
    requestData = request.get_json()
    storeId = requestData.get("id")
    print(requestData)
    result = session.query(Store).filter(Store.id == storeId).one()
    for key in requestData.keys():
        if (key != "id"):
            setattr(result, key, requestData[key])
    try:
        session.commit()
        return "Update Success"
    except Exception as e:
        return e

@app.route("/store", methods=["GET", "POST", "DELETE", "PUT"])
def accessStore():
    if (request.method == "GET"):
        return getStore()
    elif (request.method == "POST"):
        return addStore()    
    elif (request.method == "DELETE"):
        return deleteStore()
    elif (request.method == "PUT"):
        return updateStore()

# =========== End store methods ===========
# Store Items

def getStoreItems():
    allStoreItems = session.query(Store).all()
    jsonStoreItems = []
    for column in allStoreItems:
        jsonStoreItems.append({
            "store_id": column.store_id,
            "dorayaki_id": column.dorayaki_id,
            "jumlah_stok": column.jumlah_stok,
        })
    return jsonify(jsonStoreItems)
    
def addStoreItem():
    requestData = request.get_json()
    insertStoreItem = StoreItem(
        store_id = requestData["store_id"],
        dorayaki_id = requestData["dorayaki_id"],
        jumlah_stok = requestData["jumlah_stok"],
    )
    session.add(insertStoreItem)
    try:
        session.commit()
        return "Post Success"
    except Exception as e:
        return e

def deleteStoreItem():
    requestData = request.get_json()
    storeId = requestData.get("store_id")
    dorayakiId = requestData.get("dorayaki_id")
    session.query(StoreItem).filter(StoreItem.store_id == storeId and 
        StoreItem.dorayaki_id == dorayakiId).delete()
    try:
        session.commit()
        return "Delete Success"
    except Exception as e:
        return e

def updateStoreItem():
    requestData = request.get_json()
    storeId = requestData.get("store_id")
    dorayakiId = requestData.get("dorayaki_id")
    result = session.query(StoreItem).filter(StoreItem.store_id == storeId and 
        StoreItem.dorayaki_id == dorayakiId).one()
    for key in requestData.keys():
        if (key == "jumlah_stok"):
            setattr(result, key, requestData[key])
    try:
        session.commit()
        return "Update Success"
    except Exception as e:
        return e

@app.route("/store_items", methods=["GET", "POST", "DELETE", "PUT"])
def accessStoreItems():
    if (request.method == "GET"):
        return getStoreItems()
    elif (request.method == "POST"):
        return addStoreItem()    
    elif (request.method == "DELETE"):
        return deleteStoreItem()
    elif (request.method == "PUT"):
        return updateStore()

# Dorayaki from store

def getDorayakiFromStore():
    requestData = request.headers
    storeId = requestData["Id"]
    jsonStoreItems = []
    fetchJoinedData = session.query(Dorayaki, StoreItem).filter(StoreItem.store_id == storeId).filter(StoreItem.store_id == storeId).filter(Dorayaki.id == StoreItem.dorayaki_id).all()
    
    for column in fetchJoinedData:
        print(column)
        jsonStoreItems.append({
            "rasa": column[0].rasa,
            "gambar": column[0].gambar.decode('ascii'),
            "dorayaki_id": column[0].id,
            
            "jumlah_stok": column[1].jumlah_stok,
            "store_id": column[1].store_id
        })
    return (jsonify(jsonStoreItems))


def transferStoreStock():
    requestData = request.get_json()
    storeIdReceiver = requestData.get("store_id_receiver")
    dorayakiIdReceiver = requestData.get("dorayaki_id")
    storeIdTransferer = requestData.get("store_id_transferer")
    dorayakiIdTransferer = requestData.get("dorayaki_id")
    transferQty = requestData.get("transferQty")

    receiver = session.query(StoreItem).filter(StoreItem.store_id == storeIdReceiver and 
        StoreItem.dorayaki_id == dorayakiIdReceiver)
    transferer = session.query(StoreItem).filter(StoreItem.store_id == storeIdTransferer and 
        StoreItem.dorayaki_id == dorayakiIdTransferer).one()

    try:
        receiver = receiver.one()
        setattr(receiver, "jumlah_stok", receiver["jumlah_stok"]+transferQty)
    except:
        session.add(StoreItem(
        store_id = requestData["store_id_receiver"],
        dorayaki_id = requestData["dorayaki_id"],
        jumlah_stok = requestData["transferQty"]
    ))  
    setattr(transferer, "jumlah_stok", transferer["jumlah_stok"]-transferQty)

    

    try:
        session.commit()
        return "Update Success"
    except Exception as e:
        return e

@app.route("/store/transfer_stock", methods=["GET","PUT"])
def accessTransferStock():
    if (request.method == "GET"):
        return getDorayakiFromStore()
    elif (request.method == "PUT"):
        return transferStoreStock()

    

