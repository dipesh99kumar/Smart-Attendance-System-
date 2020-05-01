<?php
 $db = mysqli_connect('localhost','root','','school')
 or die('Error connecting to MySQL server.');
?>

<!DOCTYPE html>
<html>

<head>
	<title>Face Recognition Attendance</title>
    <link rel="stylesheet" href="style3.css">
	<link href='https://fonts.googleapis.com/css?family=Amethysta' rel='stylesheet'>
	<link href="https://fonts.googleapis.com/css?family=Carter+One|Merienda+One|Passion+One" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
	<div class="header">
	<h1>SMART ATTENDANCE<br> SYSTEM CSEB2</h1>
	
	</div>
	<div class="topnav">
		<a href="#">PROFILE</a>
		<a href="#">INFO</a>
		<a href="#">DUES</a>
		<a href="#">EXAMINATION</a>
		<a href="#">FACULTY</a>
		<a href="#">CONTACT</a>
	</div>
	
<div class="tabular">
<table style="margin-left:auto;margin-right:auto;width:50%;font-family:monospace;font-size:20px;text-align:center;">
<div class="rowcolumn">
<tr>
<th>SLNO</th>
<th>NAME</th>
<th>PRESENT_ABSENT</th>
<th>TOTAL</th>
</tr>";
</div>
<?php
//Step2
$query = "SELECT * FROM attendance";
mysqli_query($db, $query) or die('Error querying database.');

$result = mysqli_query($db, $query);
$row = mysqli_fetch_array($result);
echo "<tr>";
echo "<td>" . $row['SLNO'] . "</td>";
echo "<td>" . $row['NAME'] . "</td>";
echo "<td>" . $row['PRESENT_ABSENT'] . "</td>";
echo "<td>" . $row['TOTAL'] . "</td>";
echo "</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['SLNO'] . "</td>";
echo "<td>" . $row['NAME'] . "</td>";
echo "<td>" . $row['PRESENT_ABSENT'] . "</td>";
echo "<td>" . $row['TOTAL'] . "</td>";
echo "</tr>";
}
echo "</table>";
?>

</table><br>
<br>
</div>
<div class="footer">
  <h2>This project is Designed By:<br><br>
      DIPESH KUMAR SINGH&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
	  GAURAV MAHAPATRO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
	  SUBHA SNIGDHA</h2>
	  <a href="#" class="fa fa-facebook"></a>
<a href="#" class="fa fa-twitter"></a>
<a href="#" class="fa fa-google"></a>
<a href="#" class="fa fa-linkedin"></a>
<a href="#" class="fa fa-youtube"></a>
<a href="#" class="fa fa-instagram"></a>
</div>
</body>

</html>