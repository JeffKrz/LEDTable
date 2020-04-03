<?php
	$f = fopen("/sys/class/thermal/thermal_zone0/temp","r");
	$temp = fgets($f);
	echo'Die CPU Temperatur betraegt '.round($temp/1000).' Grad Celsius';
	fclose($f);
?>
