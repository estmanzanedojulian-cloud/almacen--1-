import sqlite3
DB = "minimercado.db"

def conectar():
    return sqlite3.connect(DB)

def crear_tablas():
    con = conectar()
    cur = con.cursor()
#direccion
#contacto-email
#not null
    cur.execute("""
    CREATE TABLE IF NOT EXISTS proveedores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_prov TEXT UNIQUE,
        contacto TEXT,
        telefono TEXT,
        estado TEXT,
        direccion TEXT
    )
    """)
#borrar sku
#fk nombre_prov
    cur.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT UNIQUE, 
        nombre TEXT,
        categoria TEXT,
        stock INTEGER,
        stock_minimo INTEGER,
        costo REAL,
        precio REAL,
        FOREIGN KEY(nombre_prov) REFERENCES proveedores(nombre_prov) ,
        vendidos INTEGER DEFAULT 0
    )
    """)
#tabla productos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto TEXT,
        cantidad INTEGER,
        total REAL,
        ganancia REAL
    )
    """)

    con.commit()
    con.close()



# PRODUCTOS

def obtener_productos():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM productos")

    datos = cur.fetchall()
    con.close()

    return [
        {
        "sku":x[1],
        "name":x[2],
        "category":x[3],
        "stock":x[4],
        "min_stock":x[5],
        "cost":x[6],
        "price":x[7],
        "supplier":x[8],
        "sold_today":x[9]
        }
        for x in datos
    ]



def agregar_producto(p):

    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO productos
    (sku,nombre,categoria,stock,stock_minimo,costo,precio,proveedor)
    VALUES(?,?,?,?,?,?,?,?)
    """,
    (
    p["sku"],
    p["name"],
    p["category"],
    p["stock"],
    p["min_stock"],
    p["cost"],
    p["price"],
    p["supplier"]
    ))

    con.commit()
    con.close()



def eliminar_producto(sku):

    con = conectar()
    cur = con.cursor()

    cur.execute(
    "DELETE FROM productos WHERE sku=?",
    (sku,)
    )

    con.commit()
    con.close()



def actualizar_stock(sku,cantidad):

    con = conectar()
    cur = con.cursor()

    cur.execute("""
    UPDATE productos
    SET stock = stock + ?
    WHERE sku=?
    """,
    (cantidad,sku))

    con.commit()
    con.close()



def vender_producto(sku):

    con = conectar()
    cur = con.cursor()

    cur.execute("""
    UPDATE productos
    SET stock = stock - 1,
    vendidos = vendidos + 1
    WHERE sku=?
    """,
    (sku,))

    con.commit()
    con.close()



# PROVEEDORES

def obtener_proveedores():

    con=conectar()
    cur=con.cursor()

    cur.execute("SELECT * FROM proveedores")

    datos=cur.fetchall()

    con.close()


    return [
    {
    "name":x[1],
    "contact":x[2],
    "phone":x[3],
    "status":x[4]
    }
    for x in datos
    ]



def agregar_proveedor(p):

    con=conectar()
    cur=con.cursor()

    cur.execute("""
    INSERT INTO proveedores
    (nombre,contacto,telefono,estado)
    VALUES(?,?,?,?)
    """,
    (
    p["name"],
    p["contact"],
    p["phone"],
    p["status"]
    ))

    con.commit()
    con.close()