--  Create menu main_menu
INSERT INTO menu_menu (name, description) VALUES ('main_menu', 'Main menu of the site');

-- Create menu items for 'main_menu' with named URLs and descriptions
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Home', 'Main page', '/home', 'home', NULL, 1);

INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('About Us', 'About us page', '/about', 'about', NULL, 1);

INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Contact', 'Contact page', '/contact', 'contact', NULL, 1);

-- Add sub-items for 'Home'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Sub Home 1', 'Subsection 1 for Home', '/home/sub1', 'home_sub1', (SELECT id FROM menu_menuitem WHERE name = 'Home'), 1);

INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Sub Home 2', 'Subsection 2 for Home', '/home/sub2', 'home_sub2', (SELECT id FROM menu_menuitem WHERE name = 'Home'), 1);

-- Add sub-items for 'Sub Home 1'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Sub Home 1-1', 'Subsection 1-1 for Home', '/home/sub1/sub1', 'home_sub1_sub1', (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1'), 1);

INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Sub Home 1-2', 'Subsection 1-2 for Home', '/home/sub1/sub2', 'home_sub1_sub2', (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1'), 1);

-- Add sub-items for 'Sub Home 1-1'
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Sub Home 1-1-1', 'Subsection 1-1-1 for Home', '/home/sub1/sub1/sub1', 'home_sub1_sub1_sub1', (SELECT id FROM menu_menuitem WHERE name = 'Sub Home 1-1'), 1);
-- Create the 'secondary_menu'
INSERT INTO menu_menu (name, description) VALUES ('secondary_menu', 'Secondary menu of the site');

-- Create items for 'secondary_menu' with descriptions
INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Submenu 1', 'First submenu item', '/submenu1', 'submenu1', NULL, 2);

INSERT INTO menu_menuitem (name, description, url, url_name, parent_id, menu_id) 
VALUES ('Submenu 2', 'Second submenu item', '/submenu2', 'submenu2', NULL, 2);
