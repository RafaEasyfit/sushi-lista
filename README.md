# 🍣 Sushi Lista

PWA para no perder la cuenta en los restaurantes de sushi que se piden por lista:
qué platos han llegado a la mesa y cuáles faltan.

**App:** https://rafaeasyfit.github.io/sushi-lista/

## Cómo funciona

1. **Carta** — Haz una foto de la carta y pulsa *Leer con IA*: se convierte en una
   lista de platos con número, nombre, precio y categoría. También se pueden añadir
   o corregir platos a mano.
2. **Pedido** — Haz una foto de la lista que apuntáis a mano (plato + cantidad) y
   la IA la lee y monta el pedido. Se pueden hacer varias tandas: cada foto de
   lista se marca como "leída" para no duplicar. También se puede pedir tocando
   *Pedir* en la carta.
3. **Mesa** — Cada plato con su contador *llegados/pedidos*. Cuando traen algo:
   foto (la IA sugiere qué es) o un toque en el plato. Si una bandeja trae varios
   platos mezclados, se marcan varios de golpe. Lo completo se tacha solo.
4. **Puntuación** — Estrellas (1–5) en cada plato para recordar cuáles repetir.
5. **Historial** — Al empezar una visita nueva, la actual se guarda por fecha con
   platos, cantidades, notas y total.

## IA

La lectura de fotos usa la API de Claude (Anthropic) directamente desde el móvil
(cabecera `anthropic-dangerous-direct-browser-access`). La clave API se introduce
en Ajustes y se guarda solo en el dispositivo. Sin clave, todo funciona en modo
manual. Modelos: Opus 5 (por defecto), Sonnet 5 o Haiku 4.5.

## Técnica

- PWA sin dependencias: un `index.html`, service worker y manifest.
- Estado en `localStorage`, fotos en IndexedDB (reducidas a 2000 px JPEG).
- Instalable en Android desde Chrome: menú ⋮ → *Añadir a pantalla de inicio*.
