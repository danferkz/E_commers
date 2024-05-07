<script>
</script>

<template>
        <header class = "GHeader">
            <div class="logo">
                <img src="../assets/vue.svg" alt="Logo de la empresa">
            </div>
            <div class="search">
                <input type="text" placeholder="Buscar productos por nombre...">
                <button type="submit">Buscar</button>
            </div>  
            <div class="cart">
            <button type="button">Carrito</button>
            </div>
        </header>
</template>

<style>
/* Estilos generales */

.GHeader {
  background-color: #333;
  position: fixed;
  color: #fff;
  top: 0;
  left: 0;
  display: flex;
  width: 100vw
  
}

.logo img {
  height: 50px; /* Ajustar el tamaño del logo según sea necesario */
}

.search input[type="text"] {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-right: 5px;
}

.search button {
  padding: 8px 15px;
  border-radius: 5px;
  border: none;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.cart button {
  padding: 8px 15px;
  border-radius: 5px;
  border: none;
  background-color: #008CBA;
  color: white;
  cursor: pointer;
}
</style>