window.addEventListener('resize', function() {
  if (window.innerWidth < 600) {
    document.body.style.fontSize = '18px';
  } else if (window.innerWidth >= 601 && window.innerWidth <= 992) {
    document.body.style.fontSize = '22px';
  } else {
    document.body.style.fontSize = '28px';
  }
});