var center = [{type: 'Feature', properties: {balloonContentHeader: 'г. Минск, пр. Победителей, 1',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.90558, 27.55192]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г. Минск, пр. Независимости, 143/1 (ст.м. Восток)',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.93416, 27.64803]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г. Минск, ул. Кунцевщина, 2А (ст.м. Каменная горка',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.90788, 27.43676]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г. Минск, ул.Орловская',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.93256, 27.55593]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г. Минск, пр. Рокоссовского 1(Санта)',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.87486, 27.5976993]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г. Минск, Рафиева, 64',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.8626, 27.44169]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
             {type: 'Feature', properties: {balloonContentHeader: 'г.Минск, Уборевича 176',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.83508, 27.60552]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г.Минск, ул. Шаранговича, 25 (Магнит)',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.883616, 27.448654]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties: {balloonContentHeader: 'г.Минск, ул. Сурганова, 50',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.92875, 27.58724]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}},
              {type: 'Feature', properties:  {balloonContentHeader: 'г. Минск, пр-т. Победителей 84 (ТЦ Арена Сити)',
                balloonContentFooter: "Время работы: 11:00-01:00", hintContent: "Domino's"},
                geometry: {type: 'Point', coordinates: [53.93804, 27.48769]},
                options:  {iconLayout: 'default#image', iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
                icon_imagesize: [30, 42], iconImageOffset: [-3, -42]}}
        ]

ymaps.ready(init);
var   MINIMUM_TIME = 15;
function init() {

    var myMap = new ymaps.Map("map", {
            center: [53.90,27.58],
            zoom: 12,
            controls: []
        }, {
            searchControlProvider: 'yandex#search'
        }),
         cafe, metro;
    var control = myMap.controls.get('routePanelControl');

        // Создадим панель маршрутизации.
        routePanelControl = new ymaps.control.RoutePanel({
            options: {
                // Добавим заголовок панели.
                showHeader: true,
                title: "Расчет времени"
            }
        }),
        zoomControl = new ymaps.control.ZoomControl({
            options: {
                size: 'small',
                float: 'none',
                position: {
                    bottom: 145,
                    right: 10
                }
            }
        });
    // Пользователь сможет построить только автомобильный маршрут.
    routePanelControl.routePanel.options.set({
        types: {auto: true}
    });

    // Если вы хотите задать неизменяемую точку "откуда", раскомментируйте код ниже.
//    routePanelControl.routePanel.state.set({
//        fromEnabled: false,
//        from: 'ул. Веры Хоружей, 15'
//     });

    myMap.controls.add(routePanelControl).add(zoomControl);

    // Получим ссылку на маршрут.
    routePanelControl.routePanel.getRouteAsync().then(function (route) {

        // Зададим максимально допустимое число маршрутов, возвращаемых мультимаршрутизатором.
        route.model.setParams({results: 1}, true);

        // Повесим обработчик на событие построения маршрута.
        route.model.events.add('requestsuccess', function () {

            var activeRoute = route.getActiveRoute();
            if (activeRoute) {
                // Получим протяженность маршрута.
                var length = route.getActiveRoute().properties.get("distance"),
                // Вычислим стоимость доставки.
                    time = calculate(Math.round(length.value / 1000)),
                // Создадим макет содержимого балуна маршрута.
                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                        '<span style="font-weight: bold; font-style: italic">Доставка курьера через ' + time + ' мин.</span>');
                // Зададим этот макет для содержимого балуна.
                route.options.set('routeBalloonContentLayout', balloonContentLayout);
                // Откроем балун.
                activeRoute.balloon.open();
            }
        });

    });

    // Функция, вычисляющая время доставки.
    function calculate(routeLength) {
        return Math.max(((routeLength * 1.5) + 10), MINIMUM_TIME);
    }

    function findClosestObjects () {
        // Найдем в выборке кафе, ближайшее к найденной станции метро,
        // и откроем его балун.
        cafe.getClosestTo(metro.get(0)).balloon.open();

        // Будем открывать балун кафе, который ближе всего к месту клика
        myMap.events.add('click', function (event) {
            cafe.getClosestTo(event.get('coords')).balloon.open();
        });
    }

    // Описания кафе можно хранить в формате JSON, а потом генерировать
    // из описания геообъекты с помощью ymaps.geoQuery.
    cafe = ymaps.geoQuery({
        type: 'FeatureCollection',
        features: center
    // Сразу добавим точки на карту.
    }, {
    preset: 'islands#redIcon', //все метки красные
    draggable: true // и их можно перемещать
}).addToMap(myMap);

    // С помощью обратного геокодирования найдем метро "Кропоткинская".
    metro = ymaps.geoQuery(ymaps.geocode([53.90, 27.55], {kind: 'metro'}))
    // Нужно дождаться ответа от сервера и только потом обрабатывать полученные результаты.
        .then(findClosestObjects);
}

//var myPlacemark = new ymaps.Placemark([53.90,27.58], {
//         balloonContentHeader: "г.Минск, ул. Сурганова, 50",
//         balloonContentBody: '',
//         balloonContentFooter: "Время работы: 11:00-01:00",
//         hintContent: "Domono's",
//    }, {
//        iconLayout: 'default#image',
//        iconImageHref: 'https://www.dominos.by/assets/images/marker-store7e28daf3444a6b3f1441.png',
//        icon_imagesize: [30, 42],
//        iconImageOffset: [-3, -42]
//    });
//    myMap.geoObjects.add(myPlacemark);
