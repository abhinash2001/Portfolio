document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => console.log(`Navigating to ${link.href}`));
});
