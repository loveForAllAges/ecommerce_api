# ecommerce_api

Endpoint | Метод | Описание
--- | --- | ---
`/buy/<int:pk>` | `GET` | Получение Stripe Session ID выбранного Item.
`/item/<int:pk>` | `GET` | Детальная страница товара + редирект на Stripe Checkout.

## Запуск
```
docker compose build
docker compose up
```