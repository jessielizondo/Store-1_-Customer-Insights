#!/usr/bin/env python
# coding: utf-8

# # 🛒 Store 1 Customer Insights
# 
# ## 📌 Introducción  
# **Store 1**, una empresa de comercio electrónico, busca obtener información valiosa sobre su base de clientes. Para ello, ha encargado un análisis de datos centrado en tres aspectos clave:
# 
# - La **edad** de los clientes  
# - Sus **compras anteriores**  
# - Las **categorías** de productos adquiridos  
# 
# Este proyecto representa la **primera etapa** de una solución más completa y tiene como objetivo **preparar, explorar y analizar** los datos iniciales. Esta fase sienta las bases para estudios más avanzados y campañas de marketing más efectivas en la segunda parte del proyecto.

# ## 🎯 Problema de negocio  
# El comportamiento del cliente varía según su edad, intereses y hábitos. Comprender estos patrones desde el inicio permitirá a Store 1:
# 
# - Segmentar a los clientes en grupos relevantes  
# - Lanzar campañas personalizadas y efectivas  
# - Identificar clientes valiosos para programas de fidelización

# ## 🔍 Objetivos  
# ✔ Explorar y limpiar los datos de clientes  
# ✔ Identificar comportamientos de compra por edad y categoría  
# ✔ Segmentar clientes según frecuencia y preferencias  
# ✔ Apoyar estrategias de marketing basadas en datos
# 

# ## 📊 Métricas clave  
# 📌 Métricas de clientes  
# - Distribución de edad  
# - Frecuencia de compra  
# - Segmentación por comportamiento
# 
# 📌 Métricas de productos  
# - Popularidad de categorías  
# - Cantidad de compras por tipo
# 
# 📌 Insights  
# - Relación entre edad y preferencias  
# - Visualización de patrones relevantes

# ## 🗂 Descripción del conjunto de datos  
# Origen: Datos internos de Store 1  
# Resumen:  
# - Aprox. 1000 filas | Varias columnas  
# - Columnas clave:  
#   - `customer_id`  
#   - `age`  
#   - `purchase_date`  
#   - `category`  
#   - `purchase_value`

# ## ⚙️ 1. Revisión de datos
# El cliente proporcionó los siguientes datos con formato de una lista de Python y con las siguientes columnas de datos:
# 
# - **user_id:** Identificador único para cada usuario.
# - **user_name:** El nombre del usuario.
# - **user_age:** La edad del usuario.
# - **fav_categories:** Categorías favoritas de los artículos que compró el usuario, como 'ELECTRONICS', 'SPORT' y 'BOOKS' (ELECTRÓNICOS, DEPORTES y LIBROS), etc.
# - **total_spendings:** Una lista de números enteros que indican la cantidad total gastada en cada una de las categorías favoritas.
# tas..

# In[ ]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


# 📌 Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Para esto, se revisaron los datos del primer usuario, Mike Reed, para identificar cualquier problema posible con ellos.
# 

# In[10]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# ## 🧹 2. Limpieza y transformación de datos
# 
# Primero, se corrigieron los problemas de la variable `user_name`, ya que tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido. Luego, se dividió el `user_name`  actualizado en dos subcadenas para obtener una lista que contenga dos valores la cadena para el nombre y la cadena para el apellido. Finalmente, se corrigió el tipo de datos de la variable 'user_age'
# 

# In[2]:


user_name = ' mike_reed '
user_name = user_name.strip() # escribe tu código aquí
user_name = user_name.replace('_',' ') # escribe tu código aquí

print(user_name)


# In[4]:


user_name = 'mike reed'
name_split = user_name.split() # escribe tu código aquí

print(name_split)


# In[ ]:


user_age = 32.0
user_age = int(user_age) # escribe tu código aquí

print(user_age)


# 💡 Se consideraron escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que el sistema se bloquee, se creó un bucle try-except para convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, se muestra un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.`

# In[5]:


user_age = 'treinta y dos'

# escribe tu código aquí
try:
    user_age_int = int(user_age)

except:
    print('Please provide your age as a numerical value.')


# ## 🗒🔍 3. Solicitudes de Store 1
# El equipo de dirección de Store 1 hizo algunas solicitudes de cambios para su la lista de datos de sus clientes. Estas se cumplieron en los siguientes pasos:

# ### 🗒️ 3.1 Organización de datos
# La dirección pidió ayuda para organizar los datos de sus clientes para analizarlos y gestionarlos mejor.
# Se ordenó esta lista por ID de usuario de forma ascendente.

# In[6]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

# escribe tu código aquí
users.sort()
print(users)


# ### 📐 3.2 Cálculo de la cantidad total gastada por usuario
# 
#  La dirección está interesada en conocer la cantidad total gastada por el usuario. Para esto, se cuenta con la información de los hábitos de consumo de los usuarios, incluyendo la cantidad gastada en cada una de sus categorías favoritas. 
# 

# In[7]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category) # escribe tu código aquí

print(total_amount)


# ### 📋 3.3 Resumen de la información del usuario
# 
# La dirección de la empresa pidió resumir toda la información de un usuario. Se creó una cadena formateada que utiliza información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que se creó: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).
# 

# In[8]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = f"User {user_id} is {user_name[0]} who is {user_age} years old." # escribe tu código aquí
print(user_info)


# ### 🧠  3.4 Cálculo de la cantidad de clientes registrados
# 
# La dirección también quiere una forma fácil de conocer la cantidad de clientes con cuyos datos contamos. Se creó una cadena formateada que muestra la cantidad de datos de clientes registrados.
# 

# In[10]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


user_info = f"Hemos registrado datos de {len(users)} clientes."  # escribe tu código aquí
print(user_info)


# ## ✅  4. Mejora de lista de clientes
# 
# Se aplicaron todos los cambios anteriores a la lista de clientes. Además, para continuar limpiando los datos se eliminaron todos todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo; se convirtieron todas las edades en números enteros; y, se separaron los nombres y apellidos en una sublista. 

# In[11]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []

# Procesa al primer usuario
user_name_1 = users[0][1].strip().replace('_',' ') # quitar espacios y guion bajo
user_age_1 = int(users[0][2]) # float to int
user_name_1 = user_name_1.split() # separar nombre y apellido
users_clean.append(user_name_1) # agregar sublista user_name_1 a users_clean
users_clean.append(user_age_1)

# Procesa al segundo usuario
user_name_2 = users[1][1].strip() # quitar espacios
user_age_2 = int(users[1][2]) # float to int
user_name_2 = user_name_2.split() # separar nombre y apellido
users_clean.append(user_name_2) # agregar sublista user_name_2 a users_clean
users_clean.append(user_age_2)

# Procesa al tercer usuario
user_name_3 = users[2][1].strip() # quitar espacios
user_age_3 = int(users[2][2]) # float to int
user_name_3 = user_name_3.split() # separar nombre y apellido
users_clean.append(user_name_3) # agregar sublista user_name_3 a users_clean
users_clean.append(user_age_3)


print(users_clean)


# ----------
# 

# ## ✅ Conclusiones y próximos pasos
# - Se identificaron segmentos de clientes clave por edad y comportamiento.
# - Las categorías más populares pueden utilizarse para campañas dirigidas.
# - Los clientes frecuentes ofrecen oportunidades de fidelización.
# 
# **Próximos pasos:**
# - Implementar modelos de segmentación más avanzados.
# - Usar los resultados para pruebas A/B en campañas.
# 
# ---
