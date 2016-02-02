function onSearch(){
	var obj = document.getElementById("selected_engine");
	var val = document.getElementById("search_info").value;
	if (obj.selectedIndex == 0){
		window.open("https://www.baidu.com/s?tn=baidu&ie=UTF-8&wd=" + val, "_blank");
	}
	else{
		window.open("https://www.google.com.hk/#safe=strict&q=" + val, "_blank");
	}
}