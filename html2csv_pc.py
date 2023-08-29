from bs4 import BeautifulSoup
import csv

# Input HTML data
html = "<table class=\"infobox vcard\"><caption class=\"infobox-title fn org\">Inter Milan</caption><tbody><tr><td colspan=\"2\" class=\"infobox-image\"><span class=\"mw-default-size\" typeof=\"mw:File/Frameless\"><a href=\"/wiki/File:FC_Internazionale_Milano_2021.svg\" class=\"mw-file-description\"><img alt=\"Inside the inner blue circle, a cutout of the words &quot;M&quot; and &quot;I&quot; with the &quot;I&quot; cutting inside of the &quot;M&quot; around the white circle. The inner blue circle contains an outer circle in black.\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/180px-FC_Internazionale_Milano_2021.svg.png\" decoding=\"async\" width=\"180\" height=\"180\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/270px-FC_Internazionale_Milano_2021.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/360px-FC_Internazionale_Milano_2021.svg.png 2x\" data-file-width=\"512\" data-file-height=\"512\"></a></span></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Full name</th><td class=\"infobox-data\">Football Club Internazionale Milano <a href=\"/wiki/Societ%C3%A0_per_azioni\" title=\"Società per azioni\">S.p.A.</a><sup id=\"cite_ref-1\" class=\"reference\"><a href=\"#cite_note-1\">[1]</a></sup></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Nickname(s)</th><td class=\"infobox-data nickname\"><style data-mw-deduplicate=\"TemplateStyles:r1126788409\">.mw-parser-output .plainlist ol,.mw-parser-output .plainlist ul{line-height:inherit;list-style:none;margin:0;padding:0}.mw-parser-output .plainlist ol li,.mw-parser-output .plainlist ul li{margin-bottom:0}</style><div class=\"plainlist\"><ul><li><i>I Nerazzurri</i> (The Black and Blues)</li><li><i>La Beneamata</i> (The Well-Cherished One)</li><li><i>Il <a href=\"/wiki/Biscione\" title=\"Biscione\">Biscione</a></i> (The Big <a href=\"/wiki/Grass_snake\" title=\"Grass snake\">Grass Snake</a>)</li></ul></div></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Short name</th><td class=\"infobox-data nickname\">Inter</td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Founded</th><td class=\"infobox-data\">9&nbsp;March 1908<span class=\"noprint\">; 115 years ago</span><span style=\"display:none\">&nbsp;(<span class=\"bday dtstart published updated\">1908-03-09</span>)</span> (as <i>Football Club Internazionale</i>)</td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Ground</th><td class=\"infobox-data label\"><a href=\"/wiki/San_Siro\" title=\"San Siro\">Giuseppe Meazza</a></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Capacity</th><td class=\"infobox-data\">75,923</td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Owner</th><td class=\"infobox-data\"><link rel=\"mw-deduplicated-inline-style\" href=\"mw-data:TemplateStyles:r1126788409\"><div class=\"plainlist\"><ul><li><span class=\"nowrap\"><a href=\"/wiki/Suning_Holdings_Group\" title=\"Suning Holdings Group\">Suning Holdings Group</a></span> (68.55%)<sup id=\"cite_ref-Suning_2-0\" class=\"reference\"><a href=\"#cite_note-Suning-2\">[2]</a></sup><sup id=\"cite_ref-SuningGazzetta_3-0\" class=\"reference\"><a href=\"#cite_note-SuningGazzetta-3\">[3]</a></sup></li><li>LionRock Capital (31.05%)<sup id=\"cite_ref-4\" class=\"reference\"><a href=\"#cite_note-4\">[4]</a></sup></li><li><a href=\"/wiki/Pirelli\" title=\"Pirelli\">Pirelli</a> (0.37%)<sup id=\"cite_ref-Pirelli2015bilancio_5-0\" class=\"reference\"><a href=\"#cite_note-Pirelli2015bilancio-5\">[5]</a></sup></li><li>Other shareholders (0.03%)<sup id=\"cite_ref-6\" class=\"reference\"><a href=\"#cite_note-6\">[6]</a></sup></li></ul></div></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Chairman</th><td class=\"infobox-data agent\"><a href=\"/wiki/Zhang_Kangyang\" title=\"Zhang Kangyang\">Steven Zhang</a><sup id=\"cite_ref-7\" class=\"reference\"><a href=\"#cite_note-7\">[7]</a></sup></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Head coach</th><td class=\"infobox-data agent\"><a href=\"/wiki/Simone_Inzaghi\" title=\"Simone Inzaghi\">Simone Inzaghi</a></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">League</th><td class=\"infobox-data\"><a href=\"/wiki/Serie_A\" title=\"Serie A\">Serie A</a></td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\"><a href=\"/wiki/2022%E2%80%9323_Serie_A\" title=\"2022–23 Serie A\">2022–23</a></th><td class=\"infobox-data\">Serie A, 3rd of 20</td></tr><tr><th scope=\"row\" class=\"infobox-label\" style=\"white-space: nowrap; text-align:left\">Website</th><td class=\"infobox-data\"><span class=\"url\"><a rel=\"nofollow\" class=\"external text\" href=\"http://www.inter.it\">Club website</a></span></td></tr><tr><td colspan=\"2\" class=\"infobox-full-data\"></td></tr><tr><td style=\"padding: 0; background: #ffffff; text-align: center; border: 1px solid #D3D3D3;\" colspan=\"2\">\r\n<table style=\"width:100%; text-align:center;\">\r\n<tbody><tr>\r\n<td style=\"padding:0\"><div style=\"width: 100px; margin: 0 auto; padding: 0;\">\r\n<div style=\"position: relative; left: 0px; top: 0px; width: 100px; height: 135px; margin: 0 auto; padding: 0;\">\r\n<div style=\"position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color: #0041FF;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span title=\"Team colours\"><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_left_arm_internazionale2324h.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 0px; width: 31px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/31px-Kit_left_arm.svg.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/47px-Kit_left_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/62px-Kit_left_arm.svg.png 2x\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color: #000000;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/5/53/Kit_body_internazionale2324h.png\" decoding=\"async\" width=\"38\" height=\"59\" class=\"mw-file-element\" data-file-width=\"38\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 31px; top: 0px; width: 38px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/38px-Kit_body.svg.png\" decoding=\"async\" width=\"38\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/57px-Kit_body.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/76px-Kit_body.svg.png 2x\" data-file-width=\"38\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color: #000000;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/c/c3/Kit_right_arm_internazionale2324h.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 69px; top: 0px; width: 31px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/31px-Kit_right_arm.svg.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/47px-Kit_right_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/62px-Kit_right_arm.svg.png 2x\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color: #000000\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_shorts_internazionale2324h.png\" decoding=\"async\" width=\"100\" height=\"36\" class=\"mw-file-element\" data-file-width=\"100\" data-file-height=\"36\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 59px; width: 100px; height: 36px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/100px-Kit_shorts.svg.png\" decoding=\"async\" width=\"100\" height=\"36\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/150px-Kit_shorts.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/200px-Kit_shorts.svg.png 2x\" data-file-width=\"100\" data-file-height=\"36\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 95px; width: 100px; height: 40px; background-color: #000000\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/2/2a/Kit_socks_internazionale2324hl.png\" decoding=\"async\" width=\"100\" height=\"40\" class=\"mw-file-element\" data-file-width=\"100\" data-file-height=\"40\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 95px; width: 100px; height: 40px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/100px-Kit_socks_long.svg.png\" decoding=\"async\" width=\"100\" height=\"40\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/150px-Kit_socks_long.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/200px-Kit_socks_long.svg.png 2x\" data-file-width=\"100\" data-file-height=\"40\"></span></span></div>\r\n</div>\r\n<div style=\"padding-top: 0.6em; text-align: center;\"><b><a href=\"/wiki/Kit_(association_football)\" title=\"Kit (association football)\">Home colours</a></b></div>\r\n</div></td><td style=\"padding:0\"><div style=\"width: 100px; margin: 0 auto; padding: 0;\">\r\n<div style=\"position: relative; left: 0px; top: 0px; width: 100px; height: 135px; margin: 0 auto; padding: 0;\">\r\n<div style=\"position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color: #FFFFFF;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span title=\"Team colours\"><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/1/15/Kit_left_arm_internazionale2324a.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 0px; width: 31px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/31px-Kit_left_arm.svg.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/47px-Kit_left_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Kit_left_arm.svg/62px-Kit_left_arm.svg.png 2x\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color: #FFFFFF;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/3/30/Kit_body_internazionale2324a.png\" decoding=\"async\" width=\"38\" height=\"59\" class=\"mw-file-element\" data-file-width=\"38\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 31px; top: 0px; width: 38px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/38px-Kit_body.svg.png\" decoding=\"async\" width=\"38\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/57px-Kit_body.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kit_body.svg/76px-Kit_body.svg.png 2x\" data-file-width=\"38\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color: #FFFFFF;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/7/7f/Kit_right_arm_internazionale2324a.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 69px; top: 0px; width: 31px; height: 59px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/31px-Kit_right_arm.svg.png\" decoding=\"async\" width=\"31\" height=\"59\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/47px-Kit_right_arm.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Kit_right_arm.svg/62px-Kit_right_arm.svg.png 2x\" data-file-width=\"31\" data-file-height=\"59\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color: #FFFFFF\"></div>\r\n<div style=\"position: absolute; left: 0px; top: 59px; width: 100px; height: 36px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/100px-Kit_shorts.svg.png\" decoding=\"async\" width=\"100\" height=\"36\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/150px-Kit_shorts.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/af/Kit_shorts.svg/200px-Kit_shorts.svg.png 2x\" data-file-width=\"100\" data-file-height=\"36\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 95px; width: 100px; height: 40px; background-color: #FFFFFF\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/c/c5/Kit_socks_internazionale2324al.png\" decoding=\"async\" width=\"100\" height=\"40\" class=\"mw-file-element\" data-file-width=\"100\" data-file-height=\"40\"></span></span></div>\r\n<div style=\"position: absolute; left: 0px; top: 95px; width: 100px; height: 40px;\"><span class=\"mw-default-size mw-valign-top\" typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/100px-Kit_socks_long.svg.png\" decoding=\"async\" width=\"100\" height=\"40\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/150px-Kit_socks_long.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Kit_socks_long.svg/200px-Kit_socks_long.svg.png 2x\" data-file-width=\"100\" data-file-height=\"40\"></span></span></div>\r\n</div>\r\n<div style=\"padding-top: 0.6em; text-align: center;\"><b><a href=\"/wiki/Away_colours\" title=\"Away colours\">Away colours</a></b></div>\r\n</div></td></tr>\r\n</tbody></table></td></tr><tr style=\"display:none\"><td colspan=\"2\">\r\n</td></tr><tr><td colspan=\"2\" class=\"infobox-below noprint\"><span typeof=\"mw:File\"><span><img alt=\"\" src=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Soccerball_current_event.svg/33px-Soccerball_current_event.svg.png\" decoding=\"async\" width=\"33\" height=\"33\" class=\"mw-file-element\" srcset=\"//upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Soccerball_current_event.svg/50px-Soccerball_current_event.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Soccerball_current_event.svg/66px-Soccerball_current_event.svg.png 2x\" data-file-width=\"60\" data-file-height=\"60\"></span></span> <i><a href=\"/wiki/2023%E2%80%9324_Inter_Milan_season\" title=\"2023–24 Inter Milan season\">Current season</a></i></td></tr></tbody></table>"

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', class_='infobox vcard')

# Initialize data list for CSV
data = []

# Extract rows from the table
for row in table.select('tr'):
    columns = row.find_all(['th', 'td'])
    if columns:
        data.append([col.get_text(strip=True) for col in columns])

# Write CSV data to a file
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Read the CSV and reformat headers
with open('output.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    csv_data = list(reader)

reformatted_data = []
headers = csv_data[0]
for row in csv_data[1:]:
    reformatted_data.append(dict(zip(headers, row)))

# Write the reformatted data back to a CSV file
with open('reformatted_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(reformatted_data)

print("CSV conversion and reformatting completed.")