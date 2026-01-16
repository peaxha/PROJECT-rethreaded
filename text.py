<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Project ReThreaded</title>
  <link rel="stylesheet" href="style.css" />
  <link rel="icon" type="image/png" href="favicon.png" />
</head>

<body>
  <header class="hero">
    <h1>Project ReThreaded</h1>
    <p>Confidence Through Clothing for Foster Youth</p>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdk6RMAVHhKlDTmWz0yycPTGcXmKhEYwoxYRmp5nv6UQ7TwcQ/viewform" target="_blank" class="cta-button">Donate Today</a>

    <div class="slider-container">
        <div class="slides">
            <div class="slide"><img src="image1.png" alt="Project ReThreaded 1"></div>
            <div class="slide"><img src="image2.png" alt="Project ReThreaded 2"></div>
            <div class="slide"><img src="image3.png" alt="Project ReThreaded 3"></div>
            <div class="slide"><img src="image4.png" alt="Project ReThreaded 4"></div>
        </div>
        <button class="prev" onclick="moveSlide(-1)">&#10094;</button>
        <button class="next" onclick="moveSlide(1)">&#10095;</button>
    </div>
    </header>

  <section class="mission">
    <h2>Our Mission</h2>
    <p>
      We're collecting gently used clothing to support foster youth in Sacramento — helping them feel confident, empowered, and seen.
    </p>
  </section>

  <footer>
    <p>&copy; 2025 Project ReThreaded | Founded by Ava Dwyer, El Camino Fundamental High School</p>
  </footer>

  <script>
    let currentSlide = 0;
    const slidesContainer = document.querySelector('.slides');
    const totalSlides = 4;

    function updateSlider() {
        const offset = -currentSlide * 100;
        slidesContainer.style.transform = `translateX(${offset}%)`;
    }

    function moveSlide(direction) {
        currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
        updateSlider();
    }

    // Auto-play every 5 seconds
    setInterval(() => {
        moveSlide(1);
    }, 5000);
  </script>
  </body>
</html>