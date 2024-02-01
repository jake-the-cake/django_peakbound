window.addEventListener('DOMContentLoaded', () => {

})

// Function to generate a unique visitor code
function generateVisitorCode() {
  return Math.random().toString(36).substr(2, 10);
}

// Function to get or generate a visitor code
function getVisitorCode() {
  let visitorCode = localStorage.getItem('visitorCode');
  
  if (!visitorCode) {
    visitorCode = generateVisitorCode();
    localStorage.setItem('visitorCode', visitorCode);
  }

  return visitorCode;
}

// Function to log visitor information
function logVisitor() {
  const visitorCode = getVisitorCode();
  const timestamp = new Date().toISOString();
  const ipAddress = 'retrieveIpAddress(); // Implement IP address retrieval';

  // Log the information (you might want to send it to a server)
  console.log(`Visitor Code: ${visitorCode}, Timestamp: ${timestamp}, IP Address: ${ipAddress}`);
}

// Function to check if the session has expired (24 hours)
function hasSessionExpired() {
  const lastVisit = localStorage.getItem('lastVisit');
  if (!lastVisit) return true;

  const lastVisitTime = new Date(lastVisit).getTime();
  const currentTime = new Date().getTime();
  const twentyFourHours = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

  return currentTime - lastVisitTime > twentyFourHours;
}

// Function to start or resume a session
function startOrResumeSession() {
  if (hasSessionExpired()) {
    // Start a new session
    localStorage.setItem('lastVisit', new Date().toISOString());
  }

  // Log visitor information
  logVisitor();
}

// Call the function to start or resume the session
startOrResumeSession();