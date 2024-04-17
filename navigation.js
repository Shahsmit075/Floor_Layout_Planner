function navigate() {
    // Get the current file path
    var currentPath = window.location.pathname;
    var currentDirectory = currentPath.substring(0, currentPath.lastIndexOf('/'));
  
    // Construct the target file path
    var targetPath = currentDirectory + './fol1/index.html';
  
    // Navigate to the target file
    window.location.href = targetPath;
  }
  function signup() {
    // Get the current file path
    var currentPath = window.location.pathname;
    var currentDirectory = currentPath.substring(0, currentPath.lastIndexOf('/'));
  
    // Construct the target file path
    var targetPath = currentDirectory + '/index3.html';
  
    // Navigate to the target file
    window.location.href = targetPath;
  }