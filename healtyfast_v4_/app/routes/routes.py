from flask import Blueprint, render_template, request, redirect, url_for, flash, session

main_routes = Blueprint('main', __name__)

# Base de datos simulada en memoria para que el CRUD funcione inmediatamente
PRODUCTOS_BD = [
    {"id": 1, "nombre": "Industrial Platinum", "categoria": "emergency", "precio": 180000, "imagen": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?auto=format&fit=crop&w=500", "badge": "Más Vendido", "desc": "Botiquín premium de alta especificación para empresas.", "stock": 15},
    {"id": 2, "nombre": "Glow Serum Avanzado", "categoria": "skincare", "precio": 120000, "imagen": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=500", "badge": "Premium", "desc": "Ácido hialurónico puro para luminosidad natural.", "stock": 24},
    {"id": 3, "nombre": "Óleo Corporal Relajante", "categoria": "body", "precio": 78000, "imagen": "https://images.unsplash.com/photo-1617897903246-719242758050?auto=format&fit=crop&w=500", "badge": "Wellness", "desc": "Extractos concentrados de lavanda y almendras.", "stock": 10},
    {"id": 4, "nombre": "Kit Patitas Sanas", "categoria": "pets", "precio": 45000, "imagen": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=500", "badge": "Mascotas", "desc": "Bálsamo protector e hidratante para cojinetes de perros y gatos.", "stock": 30}
]

USUARIOS_BD = [
    {"correo": "admin@healthyfast.com", "nombre": "Profesor Evaluador", "rol": "administrador"},
    {"correo": "estudiante@healthyfast.com", "nombre": "Samuel Vega", "rol": "cliente"}
]

PEDIDOS_BD = [
    {"id": "HF-9482", "cliente": "Samuel Vega", "total": 258000, "estado": "Completado"},
    {"id": "HF-9483", "cliente": "Andrea Gómez", "total": 78000, "estado": "Pendiente"}
]

@main_routes.route('/')
def index():
    # Mandamos los 3 primeros productos como destacados al Home
    return render_template('index.html', productos=PRODUCTOS_BD[:3])

@main_routes.route('/productos')
def productos():
    cat = request.args.get('categoria')
    if cat:
        filtrados = [p for p in PRODUCTOS_BD if p['categoria'] == cat]
        return render_template('products.html', productos=filtrados, categoria_activa=cat)
    return render_template('products.html', productos=PRODUCTOS_BD, categoria_activa='todos')

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        rol = request.form.get('rol')
        session['usuario'] = correo
        session['rol'] = rol
        session['nombre'] = "Usuario Grado" if rol == 'cliente' else "Admin Principal"
        flash(f'¡Sesión iniciada como {rol.upper()}!', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html')

@main_routes.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('main.index'))

# --- PANEL DE ADMINISTRACIÓN (CRUD, ANALYTICS, PEDIDOS, USUARIOS) ---
@main_routes.route('/admin')
def admin_dashboard():
    if session.get('rol') != 'administrador':
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('main.index'))
    
    # Cálculos rápidos para Analytics
    total_ventas = sum(p['total'] for p in PEDIDOS_BD)
    total_stock = sum(p['stock'] for p in PRODUCTOS_BD)
    
    return render_template('admin.html', 
                           productos=PRODUCTOS_BD, 
                           usuarios=USUARIOS_BD, 
                           pedidos=PEDIDOS_BD,
                           total_ventas=total_ventas,
                           total_stock=total_stock)

@main_routes.route('/admin/producto/agregar', methods=['POST'])
def agregar_producto():
    if session.get('rol') == 'administrador':
        nuevo_id = max([p['id'] for p in PRODUCTOS_BD]) + 1 if PRODUCTOS_BD else 1
        producto = {
            "id": nuevo_id,
            "nombre": request.form.get('nombre'),
            "categoria": request.form.get('categoria'),
            "precio": int(request.form.get('precio')),
            "imagen": request.form.get('imagen') or "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=500",
            "badge": "Nuevo",
            "desc": request.form.get('desc'),
            "stock": int(request.form.get('stock'))
        }
        PRODUCTOS_BD.append(producto)
        flash('Producto agregado correctamente.', 'success')
    return redirect(url_for('main.admin_dashboard'))

@main_routes.route('/admin/producto/editar/<int:id>', methods=['POST'])
def editar_producto(id):
    if session.get('rol') == 'administrador':
        for p in PRODUCTOS_BD:
            if p['id'] == id:
                p['nombre'] = request.form.get('nombre')
                p['categoria'] = request.form.get('categoria')
                p['precio'] = int(request.form.get('precio'))
                p['stock'] = int(request.form.get('stock'))
                p['desc'] = request.form.get('desc')
                flash('Producto actualizado.', 'success')
                break
    return redirect(url_for('main.admin_dashboard'))

@main_routes.route('/admin/producto/eliminar/<int:id>')
def eliminar_producto(id):
    global PRODUCTOS_BD
    if session.get('rol') == 'administrador':
        PRODUCTOS_BD = [p for p in PRODUCTOS_BD if p['id'] != id]
        flash('Producto eliminado de la base de datos.', 'warning')
    return redirect(url_for('main.admin_dashboard'))

