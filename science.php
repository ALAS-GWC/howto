<?php
if($_POST["message"]) {
    mail("howtohs.alas@gmail.com", "Form to email message", $_POST["message"], "From: an@email.address");
}
?>

<html>
    <head>
      <title>Science</title>
    </head>

    <body>
      <div class="topnav" id="myTopnav">
          <a href="highschool.html">Home</a>
          <a href="english.html">English</a>
          <a href="history.html">History</a>
          <a href="math.html">Math</a>
          <a href="science.html">Science</a>
          <a href="college.html">College</a>
          <a href="contact.html">Contact</a>
      </div>

    </body>

    <form action="science.php" method="post">
      <textarea name="message"></textarea>
      <input type="submit">
    </form>
<!-- <input type="submit" value="SUBMIT EMAIL TO: howtohs.alas@gmail.com" <a href="file:///Users/gwcstudent/Documents/howto/science.html"> -->

    <style>
      /* Add a black background color to the top navigation */
        .topnav {
            background-color: #333;
            overflow: hidden;
        }
        /* Style the links inside the navigation bar */
        .topnav a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }
        /* Change the color of links on hover */
        .topnav a:hover {
            background-color: #ddd;
            color: black;
        }
        /* Add a color to the active/current link */
        .topnav a.active {
            background-color: #4CAF50;
            color: white;
      }

      h1 {
        color: black;
        text-align: center;
        font-size: -webkit-xxx-large;
      }
      p {
        color: black;
        text-align: center;
        font-size: x-large;
      }
    </style>
</html>
