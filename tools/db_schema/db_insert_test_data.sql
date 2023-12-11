--  Создаем меню main_menu
INSERT INTO menu_menu (name, description) VALUES ('main_menu', 'Основное меню сайта');
--  Создаем пункты меню main_menu
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Home', 'Главная страница', '/home', NULL, NULL, 1);
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('About Us', 'Страница о нас', '/about', NULL, NULL, 1);
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Contact', 'Страница контактов', '/contact', NULL, NULL, 1);
-- Добавляем подпункты для 'Home'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Sub Home 1', 'Подраздел 1 для Главной', '/home/sub1', NULL, (SELECT id FROM menu_menuitem WHERE name = 'Home'), 1);
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Sub Home 2', 'Подраздел 2 для Главной', '/home/sub2', NULL, (SELECT id FROM menu_menuitem WHERE name = 'Home'), 1);
-- Добавляем подпункты для 'Sub Home 1'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Sub Home 1-1', 'Подраздел 1-1 для Главной', '/home/sub1/sub1', NULL, (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1'), 1);
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Sub Home 1-2', 'Подраздел 1-2 для Главной', '/home/sub1/sub2', NULL, (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1'), 1);
-- Добавляем подпункты для 'Sub Home 1-1'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Sub Home 1-1-1', 'Подраздел 1-1-1 для Главной', '/home/sub1/sub1/sub1', NULL, (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1-1'), 1);

--  Создаем меню secondary_menu
INSERT INTO menu_menu (name, description) VALUES ('secondary_menu', 'Второстепенное меню сайта');
--  Создаем пункты меню secondary_menu
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Submenu 1', 'Первый пункт подменю', '/submenu1', NULL, NULL, 2);
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) VALUES ('Submenu 2', 'Второй пункт подменю', '/submenu2', NULL, NULL, 2);
