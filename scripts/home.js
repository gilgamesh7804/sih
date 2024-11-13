// Function to handle the opening of categories (tabs)
function openCategory(evt, categoryName) {
    // Hide all content
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the active class from all tabs
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab and add the active class to the clicked tab
    document.getElementById(categoryName).style.display = "grid";
    evt.currentTarget.className += " active";
}

// Set the default tab to be opened
document.getElementById("defaultOpen").click();

let currentSlide = 0;
      const slides = document.querySelectorAll('.slider-item');
      const leftTextSection = document.getElementById('leftText');
  
      const textContent = [
        {
          title: "Delhi",
          date: "A bustling metropolis where ancient history and modern vibrancy intersect.",
          description: "Delhi’s origins date back to the legendary city of Indraprastha from the Mahabharata. Over the centuries, it has been a crucial center under various empires"
        },
        {
          title: "Rishikesh",
          date: "Rishikesh, the 'Yoga Capital of the World', offers spiritual serenity, adventure sports, and a rich cultural legacy along the sacred Ganges River.",
          description: "Rishikesh derives its name from the Sanskrit word “Hrishikesha,” meaning 'Lord of the Senses' "
        },
        {
          title: "Amritsar",
          date: "A vibrant city in Gujarat celebrated for its innovative architecture and bustling textile industry.",
          description: "Founded in 1411 by Sultan Ahmed Shah, Ahmedabad has a storied past as a major trade center and capital of the Gujarat Sultanate."
        },
        {
          title: "Hidden gems",
          date: "Explore the hidden gems of the country.",
          description: "India is a diverse country with a lot of places unique yet undiscovered.so havea look at them.."
        }
      ];
  
      function updateLeftText(index) {
        leftTextSection.innerHTML = `
          <h1>${textContent[index].title}</h1>
          <p>${textContent[index].date}</p>
          <p>${textContent[index].description}</p>
          <a href="#" class="button">KNOW MORE</a>`;
      }

    //   console.log(slides.length)
  
      function showSlide(index) {
        slides.forEach((slide, i) => {
          slide.classList.toggle('active', i === index);
        });
        updateLeftText(index);
      }
  
      function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
      }


  
      function previousSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
      }
  
      // Initialize with the first slide
      showSlide(currentSlide);