<?php

$_SERVER['HTTP_HOST'] = 'localhost';

require_once(dirname(__FILE__) . '/www/wp-load.php');
require_once(dirname(__FILE__) . '/www/wp-admin/includes/plugin.php');

update_option('siteurl', 'http://localhost/~bat/blog/');
update_option('home',    'http://localhost/~bat/blog/');

deactivate_plugins('w3-total-cache/w3-total-cache.php');

?>
