import random
import json
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enabling CORS for all routes
api = Api(app)

nflCities = [
    "Buffalo", "Miami", "New England", "New York", "Baltimore", "Cincinnati",
    "Cleveland", "Pittsburgh", "Houston", "Indianapolis", "Jacksonville",
    "Tennessee", "Denver", "Kansas City", "Las Vegas", "Los Angeles", "Dallas",
    "Philadelphia", "Washington", "Chicago", "Detroit", "Green Bay",
    "Minnesota", "Atlanta", "Carolina", "New Orleans", "Tampa Bay", "Arizona",
    "San Francisco", "Seattle", "San Diego", "Toronto", "Calgary", "Portland",
    "Oklahoma City", "London", "Paris", "Tokyo", "Barcelona", "Singapore",
    "Dubai", "Madrid", "Rome", "Hong Kong", "Beijing", "Berlin", "Melbourne",
    "Mumbai", "Orlando", "Athens", "Venice", "Mexico City", "Sydney",
    "Budapest", "Australia", "Cancun"
]

nflTeamNames = [
    "Gladiators", "Samurais", "Ninjas", "Blasters", "Hurricanes", "Skulls",
    "Mavericks", "Illusions", "Widows", "Mutants", "Tornadoes", "Avalanche",
    "Lightning", "Reapers", "Cyborgs", "Goats", "Rebels", "Skywalkers",
    "Bullets", "Warriors", "Aces", "Novas", "Lamborghinis", "Ferraris",
    "Bulls", "Mythics", "Iconics", "Hounds", "Cobras", "Furies", "Rhinos",
    "Corvettes", "Hunters", "Dragons", "Mustangs", "Avocadoes", "Knights",
    "Chairs", "MITs", "Pythons", "21ers", "FurReals", "Protractors",
    "Cabbages", "Greens", "Dogmans", "Mallas", "Turtles"
]

nflTeamColors = [
    "Blue and White", "Green and Black", "Orange and Black",
    "Yellow and Black", "Blue and Yellow", "Navy Blue and White",
    "Red and Gold", "Purple and Yellow", "Purple and Green", "Black and Gold",
    "Black and Silver", "Green and White", "Red and Black", "Red and White",
    "Red and Yellow", "Turquoise and Black", "Turquoise and White",
    "Red, White, and Blue", "Orange, Black, and Silver",
    "Red, Black, and Yellow", "Orange, White, and Green", "Red and Blue",
    "Lime Green, White, and Black", "Light Blue, Navy Blue, and Turquoise"
]

nflCoaches = [["Sean McDermott - BUF", 2], ["Mike McDaniel - MIA", 2],
              ["Bill Belichick - NE", 2], ["Robert Saleh - NYJ", 1],
              ["John Harbaugh - BAL", 2], ["Zac Taylor - CIN", 2],
              ["Kevin Stefanski - CLE", 2], ["Mike Tomlin - PIT", 2],
              ["DeMeco Ryans - HOU", 1], ["Shane Steichen - IND", 1],
              ["Doug Pederson - JAX", 2], ["Mike Vrabel - TEN", 2],
              ["Sean Payton - DEN", 2], ["Andy Reid - KC", 2],
              ["Josh McDaniels - LV", 1], ["Brandon Staley - LAC", 2],
              ["Mike McCarthy - DAL", 2], ["Brian Daboll - NYG", 2],
              ["Nick Sirianni - PHI", 2], ["Ron Rivera - WAS", 1],
              ["Matt Eberflus - CHI", 1], ["Dan Campbell - DET", 2],
              ["Matt LaFleur - GB", 2], ["Kevin O'Connell - MIN", 2],
              ["Arthur Smith - ATL", 2], ["Frank Reich - CAR", 1],
              ["Dennis Allen - NO", 1], ["Todd Bowles - TB", 1],
              ["Jonathan Gannon - ARI", 1], ["Sean McVay - LAR", 2],
              ["Kyle Shanahan - SF", 2], ["Pete Carroll - SEA", 2]]

nflMadeupCEOs = [
    "Brad Pitt", "James Bond", "Tom Cruise", "Travis Scott", "Kanye West",
    "Eminem", "Batman", "The Joker", "Vin Diesel", "Captain America",
    "Thanos's great great great grandfather", "Joe", "Elon Bezos",
    "Duck Goose", "Water Boy", "Fisherman", "Zombie",
    "The guy who created the megaknight character in Clash Royale", "You",
    "No one", "Dad", "Unknown", "Who?", "Dr.No", "BigBadWolf",
    "EthanEthanEthanEthanEthanEthan", "Jeff Sunday", "Mr.IAMNOONE",
    "Slenderman", "Mothman", "Rerry Jice", "Bom Trady", "Raron Aodgers",
    "formernamericanfootballplayerwhoplayedforthehoustonoilers", "Hi", "Me",
    "Voldemort", "Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas",
    "Your best friend", "That person sitting right next to you", "Hacker",
    "ISUCKATBUSINESS", "GorrilaGorilla", "E", "PuffinCurry",
    "anaverageiphoneuser2.0", "Dwayne Johnson"
]

nflStartQbs = [["Josh Allen - BUF", 10], ["Tua Tagovailoa - MIA", 7],
               ["Mac Jones - NE", 6], ["Aaron Rodgers - NYJ", 8],
               ["Lamar Jackson - BAL", 9], ["Joe Burrow - CIN", 9],
               ["Deshaun Watson - CLE", 6], ["Kenny Pickett - PIT", 5],
               ["C.J. Stroud - HOU", 4], ["Anthony Richardson - IND", 4],
               ["Trevor Lawrence - JAX", 7], ["Ryan Tannehill - TEN", 6],
               ["Russell Wilson - DEN", 7], ["Patrick Mahomes - KC", 10],
               ["Jimmy Garoppolo - LV", 6], ["Justin Herbert - LAC", 9],
               ["Dak Prescott - DAL", 7], ["Daniel Jones - NYG", 7],
               ["Jalen Hurts - PHI", 10], ["Sam Howell - WAS", 5],
               ["Justin Fields - CHI", 8], ["Jared Goff - DET", 7],
               ["Jordan Love - GB", 5], ["Kirk Cousins - MIN", 7],
               ["Desmond Ridder - ATL", 4], ["Bryce Young - CAR", 4],
               ["Derek Carr - NO", 7], ["Baker Mayfield - TB", 5],
               ["Kyler Murray - ARI", 7], ["Matthew Stafford - LAR", 7],
               ["Brock Purdy - SF", 6], ["Geno Smith - SEA", 7]]

nflBackupQbs = [["Kyle Allen - BUF", 3], ["Mike White - MIA", 5],
                ["Bailey Zappe - NE", 3], ["Zach Wilson - NYJ", 3],
                ["Tyler Huntley - BAL", 7], ["Trevor Siemian - CIN", 2],
                ["Joshua Dobbs - CLE", 4], ["Mitch Trubisky - PIT", 5],
                ["Davis Mills - HOU", 3], ["Nick Foles - IND", 4],
                ["C.J. Beathard - JAX", 3], ["Malik Willis - TEN", 4],
                ["Jarrett Stidham - DEN", 4], ["Blaine Gabbert - KC", 3],
                ["Brian Hoyer - LV", 3], ["Easton Stick - LAC", 3],
                ["Cooper Rush - DAL", 7], ["Tyrod Taylor - NYG", 4],
                ["Marcus Mariota - PHI", 4], ["Jacoby Brissett - WAS", 5],
                ["PJ Walker - CHI", 4], ["Nate Sudfeld - DET", 3],
                ["Sean Clifford - GB", 2], ["Nick Mullens - MIN", 3],
                ["Taylor Heinicke - ATL", 5], ["Andy Dalton - CAR", 4],
                ["Jameis Winston - NO", 5], ["Kyle Trask - TB", 2],
                ["Colt McCoy - ARI", 4], ["Brett Rypien - LAR", 3],
                ["Trey Lance - SF", 5], ["Drew Lock - SEA", 3]]

nflRbs = [["James Cook - BUF", 6], ["Raheem Mostert - MIA", 7],
          ["Rhamondre Stevenson - NE", 7], ["Breece Hall - NYJ", 7],
          ["J.K. Dobbins - BAL", 6], ["Joe Mixon - CIN", 8],
          ["Nick Chubb - CLE", 8], ["Najee Harris - PIT", 7],
          ["Dameon Pierce - HOU", 7], ["Johnathan Taylor - IND", 8],
          ["Travis Etienne Jr. - JAX", 7], ["Derrick Henry - TEN", 10],
          ["Javonte Williams - DEN", 7], ["Isiah Pacheco - KC", 7],
          ["Josh Jacobs - LV", 9], ["Austin Ekeler - LAC", 10],
          ["Tony Pollard - DAL", 8], ["Saquon Barkley - NYG", 9],
          ["D'Andre Swifth - PHI", 8], ["Brian Robinson Jr. - WAS", 6],
          ["Khalil Herbert - CHI", 6], ["David Montgomery - DET", 8],
          ["Aaron Jones - GB", 9], ["Alexander Mattison - MIN", 7],
          ["Bijan Robinson - ATL", 7], ["Miles Sanders - CAR", 8],
          ["Alvin Kamara - NO", 7], ["Rachaad White - TB", 7],
          ["James Conner - ARI", 6], ["Cam Akers - LAR", 7],
          ["Christian McCaffrey - SF", 9], ["Kenneth Walker III - SEA", 8]]

nflRb2s = [["Damein Harris - BUF", 6], ["Jeff Wilson Jr. - MIA", 5],
           ["Pierre Strong Jr. - NE", 4], ["Michael Carter Jr. - NYJ", 5],
           ["Gus Edwards - BAL", 6], ["Chase Brown - CIN", 4],
           ["Jerome Ford - CLE", 5], ["Jaylen Warren - PIT", 3],
           ["Devin Singletary - HOU", 6], ["Zack Moss - IND", 4],
           ["JaMycal Hasty - JAX", 6], ["Hassan Haskins - TEN", 5],
           ["Samaje Perine - DEN", 6], ["Clyde Edwards-Helaire - KC", 7],
           ["Zamir White - LV", 4], ["Joshua Kelley - LAC", 4],
           ["Malik Davis - DAL", 6], ["Matt Breida - NYG", 4],
           ["Rashaad Penny - PHI", 6], ["Antonio Gibson - WAS", 7],
           ["D'Onta Foreman - CHI", 6], ["Jahmyr Gibbs - DET", 5],
           ["A.J. Dillon - GB", 7], ["Ty Chandler - MIN", 4],
           ["Cordarrelle Patterson - ATL", 7], ["Chuba Hubbard - CAR", 6],
           ["Jamaal Williams - NO", 7], ["Chase Edmonds - TB", 5],
           ["Corey Clement - ARI", 5], ["Kyren Williams - LAR", 4],
           ["Elijah Mitchell - SF", 6], ["Zach Charbonnet - SEA", 4]]

nflFbs = [["Reggie Gilliam - BUF", 7], ["Alec Ingold - MIA", 6],
          ["Nick Bawden - NYJ", 3], ["Patrick Ricard - BAL", 10],
          ["Connor Heyward - PIT", 4], ["Andrew Beck - HOU", 4],
          ["Derek Parish", 2], ["Tory Carter - TEN", 3],
          ["Michael Burton - DEN", 8], ["Jakob Johnson - LV", 5],
          ["Zander Horvath - LAC", 4], ["Hunter Luepke - DAL", 2],
          ["Chris Myarick - NYG", 1], ["Alex Armah - WAS", 3],
          ["Khari Blasingame - CHI", 5], ["Jason Cabinda - DET", 4],
          ["Henry Pearson - GB", 2], ["C.J. Ham - MIN", 9],
          ["Keith Smith - ATL", 3], ["Giovanni Ricci - CAR", 4],
          ["Adam Prentice - NO", 5], ["Kyle Juszczyk - SF", 10],
          ["Nick Bellore - SEA", 7]]

nflWr1s = [["Stefon Diggs - BUF", 9], ["Tyreek Hill - MIA", 10],
           ["JuJu Smith-Schuster - NE", 7], ["Garrett Wilson - NYJ", 8],
           ["Rashod Bateman - BAL", 6], ["Ja'Marr Chase - CIN", 9],
           ["Amari Cooper - CLE", 8], ["Diontae Johnson - PIT", 7],
           ["Robert Woods - HOU", 6], ["Michael Pittman Jr. - IND", 7],
           ["Christian Kirk - JAX", 7], ["Treylon Burks - TEN", 5],
           ["Jerry Jeudy - DEN", 7], ["Marquez Valdes-Scantling - KC", 6],
           ["Davante Adams - LV", 10], ["Keenan Allen - LAC", 9],
           ["CeeDee Lamb - DAL", 9], ["Isaiah Hodgins - NYG", 6],
           ["A.J. Brown - PHI", 9], ["Terry McLaurin - WAS", 8],
           ["D.J. Moore - CHI", 7], ["Amon-Ra St. Brown - DET", 8],
           ["Christian Watson - GB", 7], ["Justin Jefferson - MIN", 10],
           ["Drake London - ATL", 7], ["Adam Thielen - CAR", 7],
           ["Michael Thomas - NO", 8], ["Mike Evans - TB", 8],
           ["Marquise Brown - ARI", 7], ["Cooper Kupp - LAR", 10],
           ["Deebo Samuel - SF", 8], ["DK Metcalf - SEA", 8]]

nflWr2s = [["Gabriel Davis - BUF", 7], ["Jaylen Waddle - MIA", 8],
           ["DeVante Parker - NE", 6], ["Allen Lazard - NYJ", 6],
           ["Odell Beckham Jr. - BAL", 7], ["Tee Higgins - CIN", 8],
           ["Donovan Peoples-Jones - CLE", 6], ["George Pickens - PIT", 6],
           ["Nico Collins - HOU", 4], ["Alec Pierce - IND", 6],
           ["Calvin Ridley - JAX", 6], ["Nick Westbrook-Ikhine - TEN", 5],
           ["Courtland Sutton - DEN", 7], ["Kadarius Toney - KC", 6],
           ["Jakobi Meyers - LV", 6], ["Mike Williams - LAC", 8],
           ["Brandin Cooks - DAL", 7], ["Parris Campbell - NYG", 6],
           ["Devonta Smith - PHI", 8], ["Jahan Dotson - WAS", 7],
           ["Darnell Mooney - CHI", 7], ["Jameson Williams - DET", 6],
           ["Romeo Doubs - GB", 6], ["K.J. Osborn - MIN", 7],
           ["Mack Hollins - ATL", 6], ["D.J. Chark - CAR", 7],
           ["Chris Olave - NO", 7], ["Chris Godwin - TB", 7],
           ["Rondale Brown - ARI", 6], ["Van Jefferson - LAR", 6],
           ["Brandon Aiyuk - SF", 7], ["Tyler Lockett - SEA", 8]]

nflWr3s = [["Khalil Shakir - BUF", 5], ["Cedrick Wilson Jr. - MIA", 5],
           ["Tyquan Thornton - NE", 3], ["Mecole Hardman Jr. - NYJ", 6],
           ["Zay Flowers - BAL", 5], ["Tyler Boyd - CIN", 7],
           ["Elijah Moore - CLE", 6], ["Allen Robinson II - PIT", 6],
           ["John Metchie III - HOU", 4], ["Josh Downs - IND", 4],
           ["Zay Jones - JAX", 6], ["Kyle Philips - TEN", 4],
           ["Tim Patrick - DEN", 5], ["Skyy Moore - KC", 5],
           ["Hunter Renfrow - LV", 6], ["Joshua Palmer - LAC", 6],
           ["Michael Gallup - DAL", 7], ["Darius Slayton - NYG", 6],
           ["Quez Watkins - PHI", 7], ["Curtis Samuel - WAS", 7],
           ["Chase Claypool - CHI", 6], ["Marvin Jones Jr. - DET", 7],
           ["Jayden Reed - GB", 4], ["Jordan Addison - MIN", 5],
           ["Scotty Miller - ATL", 5], ["Terrace Marshall Jr. - CAR", 5],
           ["Rashid Shaheed - NO", 6], ["Russell Gage - TB", 5],
           ["Greg Dortch - ARI", 5], ["Ben Skowronek - LAR", 4],
           ["Jauan Jennings - SF", 5], ["Jaxon Smith-Njigba - SEA", 5]]

nflTes = [["Dawson Knox - BUF", 6], ["Durham Smythe - MIA", 4],
          ["Hunter Henry - NE", 5], ["Tyler Conklin - NYJ", 4],
          ["Mark Andrews - BAL", 8], ["Irv Smith Jr. - CIN", 5],
          ["David Njoku - CLE", 7], ["Pat Freiermuth - PIT", 6],
          ["Dalton Schultz - HOU", 7], ["Jelani Woods - IND", 6],
          ["Evan Engram - JAX", 7], ["Chigoziem Okonkwo - TEN", 7],
          ["Greg Dulcich - DEN", 6], ["Travis Kelce - KC", 10],
          ["Austin Hooper - LV", 6], ["Gerald Everett - LAC", 7],
          ["Jake Ferguson - DAL", 6], ["Darren Waller - NYG", 8],
          ["Dallas Goedert - PHI", 7], ["Logan Thomas - WAS", 5],
          ["Cole Kmet - CHI", 7], ["Brock Wright - DET", 6],
          ["Luke Musgrave - GB", 4], ["T.J. Hockenson - MIN", 8],
          ["Kyle Pitts - ATL", 7], ["Hayden Hurst - CAR", 7],
          ["Juwan Johnson - NO", 6], ["Cade Otton - TB", 5],
          ["Zach Ertz - ARI", 7], ["Tyler Higbee - LAR", 7],
          ["George Kittle - SF", 9], ["Colby Parkinson - SEA", 6]]

nflOts = [["Dion Dawkins - BUF", 8], ["Spencer Brown - BUF", 6],
          ["Terron Armstead - MIA", 8], ["Austin Jackson - MIA", 4],
          ["Riley Reiff - NE", 5], ["Trent Brown - NE", 6],
          ["Duane Brown - NYJ", 3], ["Mekhi Becton - NYJ", 6],
          ["Ronnie Stanley - BAL", 8], ["Morgan Moses - BAL", 6],
          ["Orlando Brown Jr. - CIN", 8], ["Jonah Williams - CIN", 5],
          ["Jedrick Wills Jr. - CLE", 6], ["Jack Conklin - CLE", 6],
          ["Dan Moore Jr. - PIT", 5], ["Chukwuma Okorafor - PIT", 2],
          ["Laremy Tunsil - HOU", 8], ["Tytus Howard - HOU", 7],
          ["Bernhard Raimann - IND", 3], ["Braden Smith - IND", 6],
          ["Cam Robinson - JAX", 6], ["Walker Little - JAX", 5],
          ["Andre Dillard - TEN", 5], ["Nicholas Petit-Frere - TEN", 4],
          ["Garett Bolles - DEN", 8], ["Mike McGlinchey - DEN", 6],
          ["Jawaan Taylor - KC", 7], ["Donovan Smith - KC", 5],
          ["Kolton Miller - LV", 6], ["Jermaine Eluemunor - LV", 5],
          ["Rashawn Slater - LAC", 7], ["Trey Pipkins III - LAC", 5],
          ["Tyron Smith - DAL", 8], ["Terence Steele Jr. - DAL", 6],
          ["Andrew Thomas - NYG", 7], ["Evan Neal - NYG", 6],
          ["Jordan Mailata - PHI", 7], ["Lane Johnson - PHI", 8],
          ["Charles Leno Jr. - WAS", 6], ["Andrew Wylie - WAS", 6],
          ["Darnell Wright - CHI", 4], ["Braxton Jones - CHI", 5],
          ["Taylor Decker - DET", 6], ["Penei Sewell - DET", 8],
          ["David Bakhtiari - GB", 8], ["Zach Tom - GB", 4],
          ["Christian Darrisaw - MIN", 8], ["Brian O'Neill - MIN", 7],
          ["Jake Matthews - ATL", 7], ["Kaleb McGary - ATL", 7],
          ["Ikem Ekwonu - CAR", 7], ["Taylor Moton - CAR", 6],
          ["Trevor Penning - NO", 6], ["Ryan Ramczyk - NO", 7],
          ["Luke Goedeke - TB", 4], ["Tristan Wirfs - TB", 8],
          ["D.J. Humphries - ARI", 7], ["Paris Johnson Jr. - ARI", 5],
          ["Joe Noteboom - LAR", 5], ["Rob Havenstein - LAR", 6],
          ["Trent Williams - SF", 8], ["Colton McKivitz - SF", 6],
          ["Charles Cross - SEA", 6], ["Abraham Lucas - SEA", 5]]

nflOgs = [["Connor McGovern - BUF", 7], ["Ryan Bates - BUF", 3],
          ["Robert Hunt - MIA", 6], ["Liam Eichenberg - MIA", 4],
          ["Cole Strange - NE", 4], ["Mike Onwenu - NE", 5],
          ["Laken Tomlinson - NYJ", 6], ["Alijah Vera-Tucker - NYJ", 5],
          ["Ben Cleveland - BAL", 5], ["Kevin Zeitler - BAL", 7],
          ["Cordell Volson - CIN", 3], ["Alex Cappa - CIN", 6],
          ["Joel Bitonio - CLE", 8], ["Wyatt Teller - CLE", 8],
          ["Isaac Seumalo - PIT", 6], ["James Daniels - PIT", 3],
          ["Kenyon Green - HOU", 6], ["Shaq Mason - HOU", 4],
          ["Quenton Nelson - IND", 8], ["Will Fries - IND", 5],
          ["Ben Bartch - JAX", 4], ["Brandon Scherff - JAX", 7],
          ["Peter Skoronski - TEN", 4], ["Daniel Brunskill - TEN", 6],
          ["Ben Powers - DEN", 5], ["Quinn Meinerz - DEN", 4],
          ["Joe Thuney - KC", 7], ["Trey Smith - KC", 6],
          ["Dylan Parham - LV", 5], ["Alex Bars - LV", 3],
          ["Jamaree Salyer - LAC", 4], ["Zion Johnson - LAC", 6],
          ["Tyler Smith - DAL", 6], ["Zack Martin - DAL", 8],
          ["Ben Bredeson - NYG", 4], ["Mark Glowinski - NYG", 6],
          ["Landon Dickerson - PHI", 7], ["Tyler Steen - PHI", 6],
          ["Chris Paul - WAS", 4], ["Sam Cosmi - WAS", 5],
          ["Teven Jenkins - CHI", 5], ["Nate Davis - CHI", 4],
          ["Halapoulivaati Vaitai - DET", 5], ["Graham Glasgow - DET", 7],
          ["Jon Runyan - GB", 5], ["Elgton Jenkins - GB", 7],
          ["Ezra Cleveland - MIN", 7], ["Ed Ingram - MIN", 4],
          ["Matthew Bergeron - ATL", 5], ["Chris Lindstrom - ATL", 7],
          ["Brady Christensen - CAR", 5], ["Austin Corbett - CAR", 7],
          ["Andrus Peat - NO", 7], ["Cesar Ruiz - NO", 6],
          ["Cody Mauch - TB", 4], ["Matt Feiler - TB", 5],
          ["Elijah Wilkinson - ARI", 6], ["Will Hernandez - ARI", 7],
          ["Steve Avila - LAR", 5], ["Logan Bruss - LAR", 4],
          ["Aaron Banks - SF", 6], ["Spencer Burford - SF", 5],
          ["Damien Lewis - SEA", 6], ["Phil Haynes - SEA", 4]]

nflCs = [["Mitch Morse - BUF", 7], ["Connor Williams - MIA", 4],
         ["David Andrews - NE", 6], ["Connor McGovern - NYJ", 6],
         ["Tyler Linderbaum - BAL", 6], ["Ted Karras - CIN", 5],
         ["Ethan Pocic - CLE", 5], ["Mason Cole - PIT", 4],
         ["Juice Scruggs - HOU", 4], ["Ryan Kelly - IND", 7],
         ["Luke Fortner - JAX", 4], ["Aaron Brewer - TEN", 5],
         ["Lloyd Cushenberry III - DEN", 5], ["Creed Humphrey - KC", 8],
         ["Andre James - LV", 6], ["Corey Linsley - LAC", 7],
         ["Tyler Biadasz - DAL", 7], ["John Michael Schmitz Jr. - NYG", 5],
         ["Jason Kelce - PHI", 8], ["Nick Gates - WAS", 6],
         ["Cody Whitehair - CHI", 5], ["Frank Ragnow - DET", 7],
         ["Josh Myers - GB", 6], ["Garrett Bradburry - MIN", 8],
         ["Drew Dalman - ATL", 5], ["Bradley Bozeman - CAR", 8],
         ["Erik McCoy - NO", 5], ["Ryan Jensen - TB", 7],
         ["Hjalte Froholdt - ARI", 4], ["Brian Allen - LAR", 7],
         ["Jake Brendel - SF", 6], ["Evan Brown - SEA", 4]]

nflDes = [["Greg Rousseau - BUF", 7], ["Von Miller - BUF", 10],
          ["Christian Wilkins - MIA", 7], ["Emmanuel Ogbah - MIA", 6],
          ["Lawrence Guy - NE", 6], ["Deatrich Wise Jr. - NE", 5],
          ["Carl Lawson - NYJ", 7], ["John Franklin-Myers - NYJ", 6],
          ["Justin Madubuike - BAL", 6], ["Broderick Washington - BAL", 5],
          ["Sam Hubbard - CIN", 7], ["Trey Hendrickson - CIN", 9],
          ["Myles Garrett - CLE", 10], ["Za'Darius Smith - CLE", 8],
          ["Larry Ogunjobi - PIT", 7], ["Cameron Heyward - PIT", 9],
          ["Will Anderson Jr. - HOU", 5], ["Jerry Hughes - HOU", 5],
          ["Kwity Paye - IND", 7], ["Samson Ebukam - IND", 6],
          ["Folorunso Fatukasi - JAX", 6], ["Roy Robertson-Harris - JAX", 5],
          ["Jeffery Simmons - TEN", 8], ["Denico Autry - TEN", 5],
          ["Frank Clark - DEN", 7], ["Zach Allen - DEN", 7],
          ["George Karlaftis - KC", 7], ["Charles Omenihu - KC", 6],
          ["Maxx Crosby - LV", 9], ["Chandler Jones - LV", 8],
          ["Morgan Fox - LAC", 6], ["Sebastian Joseph-Day - LAC", 7],
          ["DeMarcus Lawrence - DAL", 8], ["Dorance Armstrong - DAL", 7],
          ["A'Shawn Robinson - NYG", 5], ["Leonard Williams - NYG", 8],
          ["Brandon Graham - PHI", 9], ["Josh Sweat - PHI", 6],
          ["Chase Young - WAS", 8], ["Montez Sweat - WAS", 8],
          ["DeMarcus Walker - CHI", 4], ["Trevis Gipson - CHI", 6],
          ["James Houston - DET", 6], ["Aidan Hutchinson - DET", 8],
          ["Kenny Clark - GB", 7], ["Devonte Wyatt - GB", 7],
          ["Harrison Phillips - MIN", 7], ["Dean Lowry - MIN", 5],
          ["Calais Campbell - ATL", 7], ["Grady Jarrett - ATL", 8],
          ["Derrick Brown - CAR", 7], ["Henry Anderson - CAR", 5],
          ["Cameron Jordan - NO", 9], ["Carl Granderson - NO", 5],
          ["Greg Gaines - TB", 6], ["Logan Hall - TB", 6],
          ["Jonathan Ledbetter - ARI", 5], ["Zaven Collins - ARI", 5],
          ["Kobie Turner - LAR", 4], ["Aaron Donald - LAR", 10],
          ["Drake Jackson - SF", 5], ["Nick Bosa - SF", 10],
          ["Dre'Mont Jones - SEA", 7], ["Jarran Reed - SEA", 6]]

nflDts = [["Ed Oliver - BUF", 8], ["DaQuan Jones - BUF", 6],
          ["Raekwon Davis - MIA", 6], ["Davon Godchaux - NE", 4],
          ["Quinton Jefferson - NYJ", 5], ["Quinnen Williams - NYJ", 7],
          ["Michael Pierce - BAL", 8], ["D.J. Reader - CIN", 7],
          ["B.J. Hill - CIN", 5], ["Jordan Elliott - CLE", 4],
          ["Dalvin Tomlinson - CLE", 7], ["Keean Benton - PIT", 4],
          ["Maliek Collins - HOU", 7], ["Sheldon Rankins - HOU", 6],
          ["DeForest Buckner - IND", 9], ["Grover Stewart - IND", 7],
          ["DaVon Hamilton - JAX", 5], ["Teair Tart - TEN", 5],
          ["D.J. Jones - DEN", 6], ["Derrick Nnadi - KC", 6],
          ["Chris Jones - KC", 9], ["Jerry Tillery - LV", 6],
          ["Bilal Nichols - LV", 5], ["Austin Johnson - LAC", 6],
          ["Osa Odigihizuwa - DAL", 6], ["Neville Gallimore - DAL", 5],
          ["Dexter Lawrence - NYG", 8], ["Fletcher Cox - PHI", 8],
          ["Jordan Davis - PHI", 6], ["Daron Payne - WAS", 7],
          ["Jonathan Allen - WAS", 8], ["Andrew Billings - CHI", 4],
          ["Justin Jones - CHI", 4], ["Alim McNeill - DET", 6],
          ["Isaiah Buggs - DET", 5], ["T.J. Slaton - GB", 5],
          ["Khyiris Tonga - MIN", 6], ["David Onyemata - ATL", 4],
          ["Derrick Brown - CAR", 8], ["Nathan Shepherd - NO", 5],
          ["Khalen Sanders - NO", 5], ["Vita Vea - TB", 9],
          ["Rashard Lawrence - ARI", 4], ["Leki Fotu - ARI", 4],
          ["Bobby Brown III - LAR", 5], ["Javon Hargrave - SF", 9],
          ["Arik Armstead - SF", 7], ["Bryan Mone - SEA", 5]]

nflLbs = [["Matt Milano - BUF", 8], ["A.J Klein - BUF", 5],
          ["Leonard Floyd - BUF", 7], ["Jaelen Phillips - MIA", 6],
          ["Jerome Baker - MIA", 7], ["Bradley Chubb - MIA", 8],
          ["David Long Jr. - MIA", 5], ["Matthew Judon - NE", 9],
          ["Ja'Whaun Bentley - NE", 4], ["Jahlani Tawai - NE", 3],
          ["Josh Uche - NE", 6], ["Jamien Sherwoood - NYJ", 3],
          ["C.J. Mosley - NYJ", 8], ["Quincy Williams - NYJ", 4],
          ["Tyus Bowser - BAL", 6], ["Patrick Queen - BAL", 7],
          ["Odafe Oweh - BAL", 6], ["Roquan Smith - BAL", 8],
          ["Logan Wilson - CIN", 7], ["Germaine Pratt - CIN", 7],
          ["Akeem Davis-Gaither - CIN", 5],
          ["Jeremiah Owusu-Koramoah - CLE", 7], ["Anthony Walker - CLE", 7],
          ["Sione Takitaki - CLE", 6], ["T.J. Watt - PIT", 10],
          ["Cole Holcomb - PIT", 7], ["Elandon Roberts - PIT", 5],
          ["Alex Highsmith - PIT", 9], ["Christian Harris - HOU", 4],
          ["Christian Kirksey - HOU", 6], ["Denzel Perryman - HOU", 7],
          ["Shaquille Leonard - IND", 8], ["E.J. Speed - IND", 4],
          ["Zaire Franklin - IND", 3], ["Josh Allen - JAX", 8],
          ["Devin Lloyd - JAX", 7], ["Foyesade Oluokun - JAX", 7],
          ["Travon Walker - JAX", 6], ["Harold Landry III - TEN", 7],
          ["Arden Key - TEN", 6], ["Monty Rice - TEN", 5],
          ["Azeez-Al Shaair - TEN", 6], ["Baron Browning - DEN", 5],
          ["Alex Singleton - DEN", 6], ["Josey Jewell - DEN", 6],
          ["Randy Gregory - DEN", 7], ["Nick Bolton - KC", 8],
          ["Drue Tranquill - KC", 6], ["Willie Gay - KC", 7],
          ["Luke Masterson - LV", 4], ["Robert Spillane - LV", 5],
          ["Divine Deablo - LV", 5], ["Joey Bosa - LAC", 9],
          ["Kenneth Murray Jr. - LAC", 8], ["Eric Kendricks - LAC", 8],
          ["Khalil Mack - LAC", 9], ["Jabril Cox - DAL", 5],
          ["Leighton Vander-Esch - DAL", 8], ["Micah Parsons - DAL", 9],
          ["Damone Clark", 4], ["Kavyon Thidobeaux - NYG", 6],
          ["Bobby Okereke - NYG", 5], ["Jarrad Davis - NYG", 5],
          ["Azeez Ojulari - NYG", 7], ["Nicholas Morrow - PHI", 6],
          ["Nakobe Dean - PHI", 7], ["Haason Reddick - PHI", 9],
          ["Cody Barton - WAS", 7], ["Jamin Davis - WAS", 7],
          ["David Mayo - WAS", 5], ["T.J. Edwards - CHI", 6],
          ["Tremaine Edmunds - CHI", 7], ["Jack Sanborn - CHI", 4],
          ["Malcolm Rodriguez - DET", 4], ["Alex Anzalone - DET", 5],
          ["Jack Campbell - DET", 5], ["Preston Smith - GB", 8],
          ["De'Vondre Campbell - GB", 8], ["Quay Walker - GB", 7],
          ["Rashan Gary - GB", 7], ["Danielle Hunter - MIN", 8],
          ["Brian Asamoah II - MIN", 5], ["Jordan Hicks - MIN", 7],
          ["Marcus Davenport - MIN", 7], ["Arnold Ebiketie - ATL", 7],
          ["Kaden Elliss - ATL", 4], ["Troy Andersen - ATL", 4],
          ["Mykal Walker - ATL", 7], ["Shaq Thompson - CAR", 7],
          ["Brian Burns - CAR", 9], ["Frankie Luvu - CAR", 7],
          ["Yetur Gross-Matos - CAR", 6], ["Pete Werner - NO", 6],
          ["Demario Davis - NO", 8], ["Zach Baun - NO", 5],
          ["Joe Tryon-Shoyinka - TB", 5], ["Devin White - TB", 9],
          ["Lavonte David - TB", 8], ["Shaquil Barrett - TB", 8],
          ["Dennis Gardeck - ARI", 4], ["Kyzir White - ARI", 5],
          ["Isaiah Simmons - ARI", 8], ["Byron Young - LAR", 5],
          ["Ernest Jones - LAR", 6], ["Christian Rozeboom - LAR", 4],
          ["Michael Hoecht - LAR", 4], ["Dre Greenlaw - SF", 7],
          ["Fred Warner - SF", 9], ["Oren Burks - SF", 5],
          ["Darrell Taylor - SEA", 6], ["Jordyn Brooks - SEA", 7],
          ["Bobby Wagner - SEA", 8], ["Uchenna Nwosu - SEA", 7]]

nflCb1s = [["Tre'Davious White - BUF", 7], ["Xavien Howard - MIA", 9],
           ["Jonathan Jones - NE", 7], ["Sauce Gardner Jr. - NYJ", 9],
           ["Marlon Humphrey - BAL", 7], ["Chidobe Awuzie - CIN", 7],
           ["Denzel Ward - CLE", 8], ["Patrick Peterson - PIT", 7],
           ["Derek Stingley Jr. - HOU", 6], ["Kenny Moore II - IND", 7],
           ["Tyson Campbell - JAX", 7], ["Roger McCreary - TEN", 6],
           ["Pat Surtain II - DEN", 8], ["Trent McDuffie - KC", 6],
           ["Nate Hobbs - LV", 7], ["J.C. Jackson - LAC", 7],
           ["Trevon Diggs - DAL", 8], ["Adoree' Jackson - NYG", 7],
           ["Darius Slay - PHI", 9], ["Kendall Fuller - WAS", 7],
           ["Jaylon Johnson - CHI", 7], ["Cameron Sutton - DET", 7],
           ["Jaire Alexander - GB", 9], ["Andrew Booth Jr. - MIN", 6],
           ["A.J. Terrell - ATL", 8], ["Donte Jackson - CAR", 8],
           ["Marshon Lattimore - NO", 8], ["Carlton Davis III - TB", 7],
           ["Rashad Fenton - ARI", 6], ["Robert Rochell - LAR", 5],
           ["Charvarius Ward - SF", 7], ["Tariq Woolen - SEA", 9]]

nflCb2s = [["Kaiir Elam - BUF", 6], ["Jalen Ramsey - MIA", 7],
           ["Christian Gonzalez - NE", 5], ["D.J. Reed - NYJ", 7],
           ["Rock Ya-Sin - BAL", 6], ["Cam Taylor-Britt - CIN", 6],
           ["Greg Newsome II - CLE", 7], ["Joey Porter Jr. - PIT", 5],
           ["Shaquill Griffin - HOU", 4], ["Julius Brents - IND", 4],
           ["Darious Williams - JAX", 6], ["Krisitan Fulton - TEN", 6],
           ["Damarri Mathis - DEN", 5], ["L'Jarius Sneed - KC", 7],
           ["Duke Shelley - LV", 5], ["Asante Samuel Jr. - LAC", 7],
           ["Stephon Gilmore - DAL", 7], ["Deonte Banks - NYG", 5],
           ["James Bradberry - PHI", 8], ["Emmanuel Forbes - WAS", 5],
           ["Kyler Gordon - CHI", 5], ["Emmanuel Moseley - DET", 6],
           ["Rasul Douglas - GB", 5], ["Byron Murphy Jr. - MIN", 5],
           ["Casey Hayward Jr. - ATL", 6], ["Jaycee Horn - CAR", 7],
           ["Paulson Adebo - NO", 7], ["Jamel Dean - TB", 7],
           ["Marco Wilson - ARI", 5], ["Cobie Durant - LAR", 5],
           ["Deommodore Lenoir - SF", 5], ["Mike Jackson - SEA", 6]]

nflSss = [["Jordan Poyer - BUF", 9], ["DeShon Elliot - MIA", 5],
          ["Kyle Dugger - NE", 7], ["Jordan Whitehead - NYJ", 6],
          ["Kyle Hamilton - BAL", 7], ["Nick Scott - CIN", 5],
          ["Grant Delpit - CLE", 6], ["Damontae Kazee - PIT", 6],
          ["Jimmie Ward - HOU", 7], ["Rodney Thomas II - IND", 5],
          ["Rayshawn Jenkins - JAX", 6], ["Amani Hooker - TEN", 6],
          ["Kareem Jackson - DEN", 6], ["Justin Reid - KC", 8],
          ["Marcus Epps - LV", 6], ["Derwin James Jr. - LAC", 9],
          ["Jayron Kearse - DAL", 7], ["Bobby McCain - NYG", 6],
          ["Terrell Edmunds - PHI", 7], ["Kamren Curl - WAS", 7],
          ["Jaquan Brisker - CHI", 7], ["C.J. Gardner-Johnson - DET", 8],
          ["Jonathan Owens - GB", 5], ["Harrison Smith - MIN", 9],
          ["Jeff Okudah - ATL", 5], ["Vonn Bell - CAR", 7],
          ["Marcus Maye - NO", 7], ["Antoine Winfield Jr. - TB", 8],
          ["Jalen Thompson - ARI", 6], ["Jordan Fuller - LAR", 7],
          ["Talanoa Hufanga - SF", 8], ["Jamal Adams - SEA", 7]]

nflFss = [["Micah Hyde - BUF", 7], ["Jevon Holland - MIA", 6],
          ["Jabrill Peppers - NE", 6], ["Adrian Amos - NYJ", 7],
          ["Marcus Williams - BAL", 8], ["Dax Hill - CIN", 5],
          ["Juan Thornhill - CLE", 7], ["Minkah Fitzpatrick - PIT", 9],
          ["Jalen Pitre - HOU", 6], ["Julian Blackmon - IND", 6],
          ["Andre Cisco - JAX", 6], ["Kevin Byard - TEN", 9],
          ["Justin Simmons - DEN", 8], ["Mike Edwards - KC", 5],
          ["Tre'Von Moehrig - LV", 6], ["Alohi Gilamn - LAC", 5],
          ["Donovan Wilson - DAL", 6], ["Xavier McKinney - NYG", 7],
          ["Reed Blankenship - PHI", 6], ["Darrick Forest - WAS", 5],
          ["Eddie Jackson - CHI", 8], ["Tracy Walker III - DET", 6],
          ["Darnell Savage - GB", 7], ["Camryn Bynum - MIN", 4],
          ["Jessie Bates III - ATL", 8], ["Xavier Woods - CAR", 6],
          ["Tyrann Mathieu - NO", 7], ["Nolan Turner - TB", 5],
          ["Budda Baker - ARI", 8], ["Russ Yeast - LAR", 4],
          ["Tashaun Gipson Jr. - SF", 7], ["Quandre Diggs - SEA", 8]]

nflKs = [["Tyler Bass - BUF", 4], ["Jason Sanders - MIA", 4],
         ["Chad Ryland - NE", 3], ["Greg Zuerlein - NYJ", 4],
         ["Justin Tucker - BAL", 5], ["Evan McPherson - CIN", 5],
         ["Cade York - CLE", 4], ["Chris Boswell - PIT", 4],
         ["Ka'imi Fairbairn - HOU", 3], ["Matt Gay - IND", 5],
         ["Brandon McManus - JAX", 5], ["Caleb Shudak - TEN", 1],
         ["Elliot Fry - DEN", 2], ["Harrison Butker - KC", 5],
         ["Daniel Carlson - LV", 5], ["Cameron Dicker - LAC", 4],
         ["Tristan Vizcaino - DAL", 3], ["Graham Gano - NYG", 4],
         ["Jake Elliott - PHI", 4], ["Joey Slye - WAS", 3],
         ["Cairo Santos - CHI", 4], ["Riley Patterson - DET", 3],
         ["Anders Carlson - GB", 3], ["Greg Joseph - MIN", 4],
         ["Younghoe Koo - ATL", 5], ["Eddy Pineiro - CAR", 3],
         ["Wil Lutz - NO", 4], ["Chase McLaughlin - TB", 3],
         ["Matt Prater - ARI", 5], ["Tanner Brown", 3], ["Jake Moody - SF", 4],
         ["Jason Myers - SEA", 5]]

nflPs = [["Sam Martin - BUF", 3], ["Jake Bailey - MIA", 3],
         ["Bryce Baringer - NE", 2], ["Thomas Morstead - NYJ", 4],
         ["Jordan Stout - BAL", 3], ["Drue Chrisman - CIN", 2],
         ["Corey Bojorquez - CLE", 5], ["Pressley Harvin III - PIT", 5],
         ["Cameron Johnston - HOU", 3], ["Rigoberto Sanchez - IND", 4],
         ["Logan Cooke - JAX", 5], ["Ryan Stonehouse - TEN", 4],
         ["Riley Dixon - DEN", 3], ["Tommy Townsend - KC", 5],
         ["AJ Cole - LV", 5], ["JK Scott - LAC", 2], ["Bryan Anger - DAL", 5],
         ["Jamie Gillan - NYG", 2], ["Arryn Siposs - PHI", 4],
         ["Tress Way - WAS", 5], ["Trenton Gill - CHI", 1],
         ["Jack Fox - DET", 5], ["Pat O'Donnell - GB", 4],
         ["Ryan Wright - MIN", 3], ["Bradley Pinion - ATL", 4],
         ["Johnny Hekker - CAR", 5], ["Blake Gillikin - NO", 3],
         ["Jake Camarda - TB", 5], ["Nolan Cooney - ARI", 3],
         ["Ethan Evans", 3], ["Mitch Wishnowsky - SF", 4],
         ["Michael Dickson - SEA", 5]]

nflRss = [["Nyheim Hines - BUF", 6], ["Braxton Berrios - MIA", 6],
          ["Marcus Jones - NE", 5], ["Ty Montgomery - NE", 3],
          ["Mecole Hardman Jr. - NYJ", 5], ["Devin Duvernay - BAL", 6],
          ["Trent Taylor - CIN", 3], ["Charlie Jones - CIN", 2],
          ["Donovan Peoples-Jones - CLE", 4], ["Jerome Ford - CLE", 2],
          ["Gunner Olszewksi - PIT", 4], ["Desmond King II - HOU", 4],
          ["Dare Ogunbowale - HOU", 4], ["Dallis Flowers - IND", 3],
          ["Isaiah McKenzie - IND", 4], ["Jamal Agnew - JAX", 6],
          ["Julius Chestnut - TEN", 4], ["Kyle Philips - TEN", 3],
          ["Montrell Washington - DEN", 3], ["Kadarius Toney - KC", 5],
          ["Isiah Pacheco - KC", 4], ["DeAndre Carter - LV", 6],
          ["Joshua Kelley - LAC", 3], ["Kavontae Turpin - DAL", 6],
          ["Adoree' Jackson - NYG", 4], ["Gary Brightwell - NYG", 4],
          ["Britain Covey - PHI", 3], ["Boston Scott - PHI", 4],
          ["Dax Milne - WAS", 3], ["Antonio Gibson - WAS", 5],
          ["Velus Jones Jr. - CHI", 3], ["Kalif Raymond - DET", 5],
          ["Kisean Nixon - GB", 6], ["Brandon Powell - MIN", 4],
          ["Kene Nwangwu - MIN", 6], ["Avery Williams - ATL", 4],
          ["Shi Smith - CAR", 4], ["Raheem Blackshear - CAR", 4],
          ["Rashid Shaheed - NO", 4], ["Deven Thomphins - TB", 3],
          ["Greg Dortch - ARI", 4], ["Tutu Atwell - LAR", 5],
          ["Kyren Williams - LAR", 2], ["Ray-Ray McCloud - SF", 5],
          ["Freddie Swain - SEA", 6], ["DeeJay Dallas - SEA", 4]]

nflLss = [["Reid Ferguson - BUF", 2], ["Blake Ferguson - MIA", 1],
          ["Joe Cardona - NE", 2], ["Thomas Hennessy - NYJ", 1],
          ["Nick Moore - BAL", 1], ["Cal Adomitis - CIN", 1],
          ["Charley Hughlett - CLE", 2], ["Christian Kuntz - PIT", 1],
          ["Jon Weeks - HOU", 2], ["Luke Rhodes - IND", 2],
          ["Ross Matiscik - JAX", 1], ["Morgan Cox - TEN", 2],
          ["Mitchell Fraboni - DEN", 1], ["James Winchester - KC", 2],
          ["Jacob Bobenmoyer - LV", 1], ["Josh Harris - LAC", 2],
          ["Trent Sieg - DAL", 1], ["Casey Kreiter - NYG", 1],
          ["Rick Lovato - PHI", 2], ["Camaron Cheeseman - WAS", 2],
          ["Patrick Scales - CHI", 1], ["Scott Daly - DET", 2],
          ["Matthew Orzech - GB", 1], ["Andrew DePaola - MIN", 1],
          ["Liam McCullough - ATL", 1], ["J.J. Jansen - CAR", 2],
          ["Zach Wood - NO", 1], ["Zach Triner - TB", 1],
          ["Joe Fortunato - ARI", 1], ["Alex Ward - LAR", 1],
          ["Taybor Pepper - SF", 1], ["Chris Toll - SEA", 1]]

class TeamOutput(Resource):
    def get(self):
        randomNflStartQb = random.choice(nflStartQbs)
        _randomNflStartQb = str(randomNflStartQb[0])

        randomNflBackupQb = random.choice(nflBackupQbs)
        _randomNflBackupQb = str(randomNflBackupQb[0])

        randomNflRb = random.choice(nflRbs)
        _randomNflRb = str(randomNflRb[0])

        randomNflRb2 = random.choice(nflRb2s)
        _randomNflRb2 = str(randomNflRb2[0])

        randomNflFb = random.choice(nflFbs)
        _randomNflFb = str(randomNflFb[0])

        randomNflWr1 = random.choice(nflWr1s)
        _randomNflWr1 = str(randomNflWr1[0])

        randomNflWr2 = random.choice(nflWr2s)
        _randomNflWr2 = str(randomNflWr2[0])

        randomNflWr3 = random.choice(nflWr3s)
        _randomNflWr3 = str(randomNflWr3[0])

        randomNflTe = random.choice(nflTes)
        _randomNflTe = str(randomNflTe[0])

        randomNflLts = random.choice(nflOts)
        _randomNflLts = str(randomNflLts[0])
        nflOts.remove(randomNflLts)

        randomNflLgs = random.choice(nflOgs)
        _randomNflLgs = str(randomNflLgs[0])
        nflOgs.remove(randomNflLgs)

        randomNflCs = random.choice(nflCs)
        _randomNflCs = str(randomNflCs[0])

        randomNflRgs = random.choice(nflOgs)
        _randomNflRgs = str(randomNflRgs[0])

        randomNflRts = random.choice(nflOts)
        _randomNflRts = str(randomNflRts[0])

        randomNflLDes = random.choice(nflDes)
        _randomNflLDes = str(randomNflLDes[0])
        nflDes.remove(randomNflLDes)

        randomNflLDts = random.choice(nflDts)
        _randomNflLDts = str(randomNflLDts[0])
        nflDts.remove(randomNflLDts)

        randomNflRDts = random.choice(nflDts)
        _randomNflRDts = str(randomNflRDts[0])

        randomNflRDes = random.choice(nflDes)
        _randomNflRDes = str(randomNflRDes[0])

        randomNflWLbs = random.choice(nflLbs)
        _randomNflWLbs = str(randomNflWLbs[0])
        nflLbs.remove(randomNflWLbs)

        randomNflMLbs = random.choice(nflLbs)
        _randomNflMLbs = str(randomNflMLbs[0])
        nflLbs.remove(randomNflMLbs)

        randomNflSLbs = random.choice(nflLbs)
        _randomNflSLbs = str(randomNflSLbs[0])

        randomNflCb1s = random.choice(nflCb1s)
        _randomNflCb1s = str(randomNflCb1s[0])

        randomNflCb2s = random.choice(nflCb2s)
        _randomNflCb2s = str(randomNflCb2s[0])

        randomNflSss = random.choice(nflSss)
        _randomNflSss = str(randomNflSss[0])

        randomNflFss = random.choice(nflFss)
        _randomNflFss = str(randomNflFss[0])

        randomNflNickels = random.choice(nflCb2s)
        _randomNflNickels = str(randomNflNickels[0])

        randomNflDimes = random.choice(nflFss)
        _randomNflDimes = str(randomNflDimes[0])

        randomNflKs = random.choice(nflKs)
        _randomNflKs = str(randomNflKs[0])

        randomNflPs = random.choice(nflPs)
        _randomNflPs = str(randomNflPs[0])

        randomNflRss = random.choice(nflRss)
        _randomNflRss = str(randomNflRss[0])

        randomNflLss = random.choice(nflLss)
        _randomNflLss = str(randomNflLss[0])

        randomNflCities = random.choice(nflCities)
        _randomNflCities = str(randomNflCities)

        randomNflTeamNames = random.choice(nflTeamNames)
        _randomNflTeamNames = str(randomNflTeamNames)

        randomNflTeamColors = random.choice(nflTeamColors)
        _randomNflTeamColors = str(randomNflTeamColors)

        randomNflCoaches = random.choice(nflCoaches)
        _randomNflCoaches = str(randomNflCoaches[0])

        randomNflMadeupCEOs = random.choice(nflMadeupCEOs)
        _randomNflMadeupCEOs = str(randomNflMadeupCEOs)

        randomNflMadeupCEOs1 = random.choice(nflMadeupCEOs)
        _randomNflMadeupCEOs1 = str(randomNflMadeupCEOs1)

        rateAdding = randomNflStartQb[1] + randomNflBackupQb[1] + randomNflRb[
            1] + randomNflRb2[1] + randomNflFb[1] + randomNflWr1[1] + randomNflWr2[
                1] + randomNflWr3[1] + randomNflTe[1] + randomNflLts[
                    1] + randomNflLgs[1] + randomNflCs[1] + randomNflRgs[
                        1] + randomNflRts[1] + randomNflLDes[1] + randomNflLDts[
                            1] + randomNflRDts[1] + randomNflRDes[
                                1] + randomNflWLbs[1] + randomNflMLbs[
                                    1] + randomNflSLbs[1] + randomNflCb1s[
                                        1] + randomNflCb2s[1] + randomNflSss[
                                            1] + randomNflFss[1] + randomNflKs[
                                                1] + randomNflPs[1] + randomNflRss[
                                                    1] + randomNflLss[1]
        teamResponse = ''
        # Rating adjustments
        if (randomNflStartQb[0] == "Patrick Mahomes - KC" or randomNflCoaches[0] == "Andy Reid - KC"):
            rateAdding -= 60
            teamResponse = "You got either Mahomes or Reid, since they are SB champions, you get +12"
        elif randomNflStartQb[1] < 6 and rateAdding > 82 and randomNflCoaches[1] == 1:
            rateAdding -= 87
            teamResponse = "You got the QB Effect(Lose -5 to rating) because your QB is bad(has rating of 5 or below). Also, since your coach is bad, your rating decreases by 10."
        elif (randomNflStartQb[1] > 8 and rateAdding > 82 and randomNflCoaches[0] == "Andy Reid - KC"):
            rateAdding -= 62
            teamResponse = "Your QB and coach is good, +10 to rating"
        elif (randomNflStartQb[1] < 6 and rateAdding > 82 and randomNflCoaches[1] == 2):
            rateAdding -= 77
            teamResponse = "You got the QB Effect(Lose -5 to rating) because your QB is bad(has rating of 5 or below)."
        elif (randomNflStartQb[1] > 8 and rateAdding > 82):
            rateAdding -= 67
            teamResponse = "Your QB is good, +5 to rating"
        elif (randomNflStartQb[1] > 6 and rateAdding > 82 and randomNflCoaches[1] == 1):
            rateAdding -= 82
            teamResponse = "Since your coach is bad, your rating decreased by 10."
        elif randomNflStartQb[1] < 6 and rateAdding < 82 and randomNflCoaches[1] == 1:
            rateAdding = 0
            teamResponse = "You got the QB Effect(Lose -5 to rating) because your QB is bad(has rating of 5 or below). And also since your coach is bad, your rating decreased by 10. But, since you have a really low rated team, your rating will be set to 0 instead of negative rating. Negative rating would just be too brutal, wouldn't it?"
        elif (randomNflCoaches[1] == 2 and rateAdding > 192):
            rateAdding = 120
            teamResponse = "Your coach is good, so your rating increases by 5. Your rating was higher than 120 because of the coach effect, but the rating should always 120 or lower because then it would be a bit unfair don't you think?"
        else:
            rateAdding -= 72
            teamResponse = "Your team has no effects."

        team = [_randomNflCoaches, _randomNflStartQb, _randomNflBackupQb, _randomNflRb, _randomNflRb2,
                _randomNflWr1, _randomNflWr2, _randomNflWr3, _randomNflFb, _randomNflTe, _randomNflLts,
                _randomNflLgs, _randomNflCs, _randomNflRgs, _randomNflRts, _randomNflLDes, _randomNflLDts,
                _randomNflRDts, _randomNflRDes, _randomNflWLbs, _randomNflMLbs, _randomNflSLbs, _randomNflCb1s,
                _randomNflCb2s, _randomNflSss, _randomNflFss, _randomNflNickels, _randomNflDimes, _randomNflKs,
                _randomNflPs, _randomNflRss, _randomNflLss]
        

        #NFL Team Abbreviations & Teams(primarily for generateSchedule())
        nflTeams = [
            ["BUF", "Buffalo Bills"], ["MIA", "Miami Dolphins"], ["NE", "New England Patriots"], ["NYJ", "New York Jets"],
            ["BAL", "Baltimore Ravens"], ["CIN", "Cincinnati Bengals"], ["CLE", "Cleveland Browns"], ["PIT", "Pittsburgh Steelers"],
            ["HOU", "Houston Texans"], ["IND", "Indianapolis Colts"], ["JAX", "Jacksonville Jaguars"], ["TEN", "Tennessee Titans"],
            ["DEN", "Denver Broncos"], ["KC", "Kansas City Chiefs"], ["LV", "Las Vegas Raiders"], ["LAC", "Los Angeles Chargers"],
            ["DAL", "Dallas Cowboys"], ["NYG", "New York Giants"], ["PHI", "Philadelphia Eagles"], ["WAS", "Washington Commanders"],
            ["CHI", "Chicago Bears"], ["DET", "Detroit Lions"], ["GB", "Green Bay Packers"], ["MIN", "Minnesota Vikings"],
            ["ATL", "Atlanta Falcons"], ["CAR", "Carolina Panthers"], ["NO", "New Orleans Saints"], ["TB", "Tampa Bay Buccaneers"],
            ["ARI", "Arizona Cardinals"], ["LAR", "Los Angeles Rams"], ["SF", "San Francisco 49ers"], ["SEA", "Seattle Seahawks"]
        ]

        #Generate randomly generated team's schedule
        def generateSchedule():
            for x in team:
                _team = x.split()
                index = _team[len(_team) - 1]
                for i in nflTeams:
                    if index == i[0]:
                        nflTeams.remove(i)
            random.shuffle(nflTeams)
            return nflTeams

        def homeOrAway():
            number = int(random.randint(1, 10))
            if number % 2 == 0:
                homeOrAway = "Vs "
            else:
                homeOrAway = "At "
            return homeOrAway
        
        schedule_team = generateSchedule()

        x = 1
        schedule = []
        for team in schedule_team:
            scheduleDict={}
            homeAway = homeOrAway()
            scheduleDict['id'] = str(x)
            scheduleDict["item"] = "Week " + str(x) + ": " + homeAway + team[1]
            schedule.append(scheduleDict)
            x += 1

        # Determing team's ceiling, floor, and predicted record
        def ceilingFloor():
            scheduleLength = len(schedule_team)
            ceiling = ""
            floor = ""
            record = ""
            if (rateAdding < 70):
                wins = random.randint(0, int(scheduleLength/5))
                ceiling += "Ceiling: " + str(int(scheduleLength/5)) + "-" + str(scheduleLength-int(scheduleLength/5))
                floor += "Floor: 0-" + str(scheduleLength)
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            elif (rateAdding > 70 and rateAdding < 80):
                wins = random.randint(int(scheduleLength/5), int(scheduleLength/2))
                ceiling += "Ceiling: " + str(int(scheduleLength/2)) + "-" + str(scheduleLength-int(scheduleLength/2))
                floor += "Floor: " + str(int(scheduleLength/5)) + "-" + str(scheduleLength-int(scheduleLength/5))
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            elif (rateAdding > 80 and rateAdding < 90):
                wins = random.randint(int(scheduleLength/2), int(scheduleLength/1.7))
                ceiling += "Ceiling: " + str(int(scheduleLength/1.7)) + "-" + str(scheduleLength-int(scheduleLength/1.7))
                floor += "Floor: " + str(int(scheduleLength/2)) + "-" + str(scheduleLength-int(scheduleLength/2))
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            elif (rateAdding > 90 and rateAdding < 100):
                wins = random.randint(int(scheduleLength/1.7), int(scheduleLength/1.5))
                ceiling += "Ceiling: " + str(int(scheduleLength/1.5)) + "-" + str(scheduleLength-int(scheduleLength/1.5))
                floor += "Floor: " + str(int(scheduleLength/1.7)) + "-" + str(scheduleLength-int(scheduleLength/1.7))
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            elif (rateAdding > 100 and rateAdding < 110):
                wins = random.randint(int(scheduleLength/1.5), int(scheduleLength/1.1))
                ceiling += "Ceiling: " + str(int(scheduleLength/1.1)) + "-" + str(scheduleLength-int(scheduleLength/1.1))
                floor += "Floor: " + str(int(scheduleLength/1.5)) + "-" + str(scheduleLength-int(scheduleLength/1.5))
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            elif (rateAdding > 110 and rateAdding <= 120):
                wins = random.randint(int(scheduleLength/1.1), int(scheduleLength))
                ceiling += "Ceiling: " + str(int(scheduleLength)) + "-" + str(scheduleLength-int(scheduleLength))
                floor += "Floor: " + str(int(scheduleLength/1.1)) + "-" + str(scheduleLength-int(scheduleLength/1.1))
                record += "Predicted Record: " + str(wins) + "-" + str(scheduleLength-wins)
            ceilingFloor = [ceiling, floor, record]
            items = [ceilingFloor, wins]
            return items

        teamRecord = ceilingFloor() 

        y=1
        finalTeamRecord=[]
        for record in teamRecord[0]:
            recordDict={}
            recordDict['id'] = str(y)
            recordDict["item"] = record
            finalTeamRecord.append(recordDict)
            y+=1

        # Determining team's playoff chances
        def playoffChances():
            playoffChance = 0
            sbChances = 0
            winsRecord = ceilingFloor()
            totalGames = len(schedule_team)
            winRate = (winsRecord[1] / totalGames) * 100
            if (winRate >= 0.0 and winRate < 20.0):
                playoffChance += round(random.uniform(0.0, 20.0), 1)
            elif (winRate >= 20.0 and winRate < 40.0):
                playoffChance += round(random.uniform(20.0, 40.0), 1)
            elif (winRate >= 40.0 and winRate < 60.0):
                playoffChance += round(random.uniform(40.0, 60.0), 1)
            elif (winRate >= 60.0 and winRate < 80.0):
                playoffChance += round(random.uniform(60.0, 80.0), 1)
            elif (winRate >= 80.0 and winRate < 100.0):
                playoffChance += round(random.uniform(80.0, 99.0), 1)
            else:
                playoffChance += 99.9
            sbChances = playoffChance / 4
            playoffChances = ["Chance to make playoffs: " + str(playoffChance) + "%", "Chance to win Superbowl: " + str(sbChances) + "%"]
            return playoffChances

        pChances = playoffChances()
        z=1
        finalPlayoffChances=[]
        for chance in pChances:
            playoffDict={}
            playoffDict['id'] = str(z)
            playoffDict['item'] = chance
            finalPlayoffChances.append(playoffDict)
            z+=1
        


        return {
            'teamItems': [
               {'id': '1', 'item': "Team Name: " + _randomNflCities + " " + _randomNflTeamNames},
               {'id': '2', 'item': "Team CEO: " + _randomNflMadeupCEOs},
               {'id': '3', 'item': "Team GM: " + _randomNflMadeupCEOs1},
               {'id': '4', 'item': "Team Colors: " + _randomNflTeamColors},
               {'id': '5', 'item': "Coach: " + _randomNflCoaches},
               {'id': '6', 'item': "QB1: " + _randomNflStartQb},
               {'id': '7', 'item': "QB2: " + _randomNflBackupQb},
               {'id': '8', 'item': "RB1: " + _randomNflRb},
               {'id': '9', 'item': "RB2: " + _randomNflRb2},
               {'id': '10', 'item': "FB: " + _randomNflFb},
               {'id': '11', 'item': "WR1: " + _randomNflWr1},
               {'id': '12', 'item': "WR2: " + _randomNflWr2},
               {'id': '13', 'item': "WR3: " + _randomNflWr3},
               {'id': '14', 'item': "TE: " + _randomNflTe},
               {'id': '15', 'item': "LT: " + _randomNflLts},
               {'id': '16', 'item': "LG: " + _randomNflLgs},
               {'id': '17', 'item': "C: " + _randomNflCs},
               {'id': '18', 'item': "RG: " + _randomNflRgs},
               {'id': '19', 'item': "RT: " + _randomNflRts},
               {'id': '20', "item": "LDE: " + _randomNflLDes},
               {'id': '21', "item": "LDT: " + _randomNflLDts},
               {'id': '22', "item": "RDT: " + _randomNflRDts},
               {'id': '23', "item": "RDE: " + _randomNflRDes},
               {'id': '24', "item": "WLB: " + _randomNflWLbs},
               {'id': '25', "item": "MLB: " + _randomNflMLbs},
               {'id': '26', "item": "SLB: " + _randomNflSLbs},
               {'id': '27', "item": "CB1: " + _randomNflCb1s},
               {'id': '28', "item": "CB2: " + _randomNflCb2s},
               {'id': '29', "item": "SS: " + _randomNflSss},
               {'id': '30', "item": "FS: " + _randomNflFss},
               {'id': '31', "item": "Nickelback: " + _randomNflNickels},
               {'id': '32', "item": "Dimeback: " + _randomNflDimes},
               {'id': '33', "item": "K: " + _randomNflKs},
               {'id': '34', "item": "P: " + _randomNflPs},
               {'id': '35', "item": "RS: " + _randomNflRss},
               {'id': '36', "item": "LS: " + _randomNflLss},
               {'id': '37', "item": "Team Rating: " + str(rateAdding) + "/120"},
               {'id': '38', "item": teamResponse}
            ],
            'schedule': schedule,
            'record': finalTeamRecord,
            'pChances': finalPlayoffChances
        }
    
api.add_resource(TeamOutput, '/')

if __name__ == '__main__':
    app.run(debug=True)
