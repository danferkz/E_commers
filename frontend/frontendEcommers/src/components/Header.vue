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
  width: 100vw;
  justify-content: space-between; /* Add this to evenly distribute the items */
  padding: 10px; /* Add padding to create space around the items */
}

.logo {
  margin-right: auto; /* Push the logo to the left as much as possible */
}

.logo img {
  height: 50px; /* Ajustar el tamaño del logo según sea necesario */
}

.search {
  margin: 0 10px; /* Add margin to create space between elements */
}

.search input[type="text"] {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.search button {
  padding: 8px 15px;
  border-radius: 5px;
  border: none;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.cart {
  margin-left: auto; /* Push the cart button to the right as much as possible */
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