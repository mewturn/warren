function pop() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
};

function empty() {
	document.getElementById("outp").innerHTML = "翻譯中...  請稍候...";
	localStorage.setItem("selectedIndex", document.getElementById("model").selectedIndex);
};

function load() {
	if (localStorage.getItem("selectedIndex")) {
		document.getElementById("model").selectedIndex = localStorage.getItem("selectedIndex");
	};
};

function feedback() {
    document.getElementById("eng").value = document.getElementById("outp").innerHTML;
    document.getElementById("chi").value = document.getElementById("zhsrc").innerHTML;
	alert("Thank you for your feedback!");
};
