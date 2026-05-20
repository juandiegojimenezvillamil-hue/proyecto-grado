document.addEventListener("DOMContentLoaded", function () {
    // 1. Quitar Loader animado al cargar la página
    const loader = document.getElementById("pantalla-loader");
    if (loader) {
        setTimeout(() => {
            loader.style.opacity = "0";
            loader.style.visibility = "hidden";
        }, 600);
    }

    // 2. Lógica nativa de alternancia de Modo Oscuro
    const botonDark = document.getElementById("toggle-darkmode");
    if (botonDark) {
        botonDark.addEventListener("click", () => {
            const temaActual = document.documentElement.getAttribute("data-theme");
            if (temaActual === "dark") {
                document.documentElement.removeAttribute("data-theme");
                botonDark.innerHTML = '<i class="fa-solid fa-moon"></i>';
            } else {
                document.documentElement.setAttribute("data-theme", "dark");
                botonDark.innerHTML = '<i class="fa-solid fa-sun"></i>';
            }
        });
    }

    // 3. Sistema Scroll Reveal usando el API nativo de Navegadores
    const elementosReveal = document.querySelectorAll(".scroll-reveal");
    const observador = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    }, { threshold: 0.1 });

    elementosReveal.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(30px)";
        el.style.transition = "all 0.6s ease-out";
        observador.observe(el);
    });
});

// 4. Lógica de Negocio del Carrito Reactivo Lateral
let carrito = [];

function agregarAlCarrito(id, nombre, precio) {
    let existente = carrito.find(p => p.id === id);
    if (existente) {
        existente.cantidad++;
    } else {
        carrito.push({ id: id, nombre: nombre, precio: precio, cantidad: 1 });
    }
    renderizarCarrito();
}

function renderizarCarrito() {
    const cuerpo = document.getElementById("items-carrito-render");
    const contador = document.getElementById("badge-contador");
    const totalText = document.getElementById("total-precio-render");
    
    if (carrito.length === 0) {
        cuerpo.innerHTML = '<p class="text-muted text-center py-4">Bolsa vacía.</p>';
        contador.innerText = "0";
        totalText.innerText = "$0 COP";
        return;
    }
    
    let html = "";
    let total = 0;
    let unidades = 0;
    
    carrito.forEach(item => {
        total += item.precio * item.cantidad;
        unidades += item.cantidad;
        html += `
            <div class="d-flex justify-content-between align-items-center mb-2 p-2 bg-light rounded text-dark">
                <div>
                    <h6 class="m-0 small fw-bold">${item.nombre}</h6>
                    <small>${item.cantidad}x - $${item.precio.toLocaleString()} COP</small>
                </div>
                <span class="badge bg-danger rounded-pill">$${(item.precio * item.cantidad).toLocaleString()}</span>
            </div>`;
    });
    
    cuerpo.innerHTML = html;
    contador.innerText = unidades;
    totalText.innerText = `$${total.toLocaleString()} COP`;
}
