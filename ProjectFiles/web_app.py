from flask import Flask, redirect, url_for, render_template, request
from database import register_account, hashString, getAccount
import database
import utility
from random import randint

app = Flask(__name__)


# go to landing page
@app.route("/")
def landing_page():
    return render_template("LandingPage.html")


@app.route("/home")
def home():
    return render_template("LandingPage.html")


# calls the login.html, asks the user to enter email and password
@app.route("/login")
def login():
    return render_template("Login.html")


# retrieves data from login form, check if account exist in database
@app.route("/login_account", methods=['POST'])
def loginAccount():
    if getAccount(request.form["email"], hashString(request.form["psw"])):
        return render_template("LandingPage.html", account=request.form["email"])
    else:
        return "invalid"


# render bathrobes
@app.route("/productListing/<prod>")
def productListing(prod: int):
    DATA: list = []
    data: utility.Product = database.getProduct(prod)
    DATA.append(data)
    return render_template("Listing/item.html", data=DATA)

# render Bath.html
@app.route("/bath")
def bath():
    return render_template("Bath.html")


# render bath mats
@app.route("/bathmats")
def bathmats():
    DATA: list = []
    for x in range(101, 106):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("Bathmats.html", data=DATA)


# render towel
@app.route("/towel")
def towel():
    DATA: list = []
    for x in range(201, 206):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("Towels.html", data=DATA)


# render bathrobes
@app.route("/bathrobes")
def bathrobes():
    DATA: list = []
    for x in range(301, 306):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("Bathrobes.html", data=DATA)


# render bath mirrors
@app.route("/bathmirrors")
def bathmirrors():
    DATA: list = []
    for x in range(601, 606):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("BathMirrors.html", data=DATA)


# render Linen Towers & Cabinets
@app.route("/linentowers")
def linentowers():
    DATA: list = []
    for x in range(901, 906):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("LinenTowers.html", data=DATA)


# render Towel Rails & Warmers
@app.route("/towelrails")
def towelrails():
    DATA: list = []
    for x in range(1201, 1206):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("TowelRails.html", data=DATA)


# render Bathroom Counter Storage
@app.route("/bathroomcounter")
def bathroomcounter():
    DATA: list = []
    for x in range(401, 407):
        if x == 404:
            continue
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("BathroomCounter.html", data=DATA)


# render Holders & Dispensers
@app.route("/holders")
def holders():
    DATA: list = []
    for x in range(501, 506):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("Holders.html", data=DATA)


# render Shower Curtains & Accessories
@app.route("/showercurtains")
def showercurtains():
    DATA: list = []
    for x in range(1001, 1006):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("ShowerCurtains.html", data=DATA)


# render Shower Caddies & Hangers
@app.route("/showerhangers")
def showerhangers():
    DATA: list = []
    for x in range(1101, 1106):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("ShowerCaddies.html", data=DATA)


# render Bathroom Shelving
@app.route("/bathroomshelving")
def bathroomshelving():
    DATA: list = []
    for x in range(801, 806):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("BathroomShelving.html", data=DATA)


# render Bathroom Scale
@app.route("/bathroomscale")
def bathroomscale():
    DATA: list = []
    for x in range(701, 706):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    return render_template("BathroomScales.html", data=DATA)


# render Bedding.html
@app.route("/bedding")
def bedding():
    return render_template("Bedding.html")


# render Bedding Runners & Skirts
@app.route("/bedrunners")
def bedrunners():
    return render_template("BedRunners.html")


# render Bed Sheet
@app.route("/bedsheet")
def bedsheet():
    return render_template("Bedsheet.html")


# render Blankets & Throws
@app.route("/blanket")
def blanket():
    return render_template("Blankets.html")


# render Comforters, Quilts & Duvets
@app.route("/comforter")
def comforter():
    return render_template("Comforters.html")


# render Electric Blanket
@app.route("/electricblanket")
def electricblanket():
    return render_template("ElectricBlankets.html")


# render Mattress Pads
@app.route("/mattresspads")
def mattrespads():
    return render_template("MattersPads.html")


# render Pillow Cases
@app.route("/pillowcases")
def pillowcases():
    return render_template("PillowCases.html")


# render Pillow Protectors
@app.route("/pillowprotectors")
def pillowprotectors():
    return render_template("PillowProtectors.html")


# render Pillow Bolsters
@app.route("/pillowbolsters")
def pillowbolsters():
    return render_template("PillowBolsters.html")


# render Furniture.html
@app.route("/furniture")
def furniture():
    return render_template("Furniture.html")


# render Bedroom Furniture
@app.route("/bedroomfurniture")
def bedroomfurniture():
    return render_template("BedroomFurniture.html")


# render Chairs
@app.route("/chairs")
def chair():
    return render_template("Chairs.html")


# render Gaming Furniture
@app.route("/gamingfurniture")
def gamingfurniture():
    return render_template("GamingFurniture.html")


# render Home Office Furniture
@app.route("/officefurniture")
def officefurniture():
    return render_template("OfficeFurniture.html")


# render Kids Tables & Sets
@app.route("/kidstable")
def kidstable():
    return render_template("KidsTable.html")


# render Kitchen & Dining Furniture
@app.route("/kithcenfurniture")
def kithcenfurniture():
    return render_template("KitchenFurniture.html")


# render Living Room Furniture
@app.route("/livingroom")
def livingroom():
    return render_template("LivingRoom.html") \
 \
 \
# render Mattress
@app.route("/mattress")
def mattress():
    return render_template("Mattress.html")


# render Media or TV Storge
@app.route("/mediastorage")
def mediastorage():
    return render_template("MediaStorage.html")


# render Outdoor Furniture
@app.route("/outdoorfurniture")
def outdoorfurniture():
    return render_template("OutdoorFurniture.html")


# render Sofas
@app.route("/sofas")
def sofas():
    return render_template("Sofas.html")


# render Wardrobes
@app.route("/wardrobe")
def wardrobe():
    return render_template("Wardrobes.html")


# render Storage_and_Organization.html
@app.route("/storage")
def storage():
    return render_template("Storage_and_Organization.html")


# render Compression Bags
@app.route("/compressionbags")
def compressionbags():
    return render_template("CompressionBags.html")


# render Deck Boxes & Balcony Storage
@app.route("/deckboxes")
def deckboxes():
    return render_template("DeckBoxes.html")


# render Medicine & First Ais Storage
@app.route("/medicine")
def medicine():
    return render_template("Medicine.html")


# render Shoe Organiser
@app.route("/shoe")
def shoe():
    return render_template("ShoeOrganiser.html")


# render Space Savers
@app.route("/spacesavers")
def spacesavers():
    return render_template("SpaceSavers.html")


# render Storge Bins & Baskets
@app.route("/storagebins")
def storagebins():
    return render_template("StorageBins.html")


# render Wardrobe Organiser
@app.route("/wardrobeorganiser")
def wardrobeorganiser():
    return render_template("WardrobeOrganiser.html")


# render Laundry_and_Cleaning_Equipment.html
@app.route("/laundry_cleaning")
def laundry_cleaning():
    return render_template("Laundry_and_Cleaning_Equipment.html")


# render Brooms., Mops & Sweepers
@app.route("/brooms")
def brooms():
    return render_template("Brooms.html")


# render Cleaning Buckets & Tubs
@app.route("/cleaning")
def cleaning():
    return render_template("CleaningBuckets.html")


# render Clothes Hangers & Pegs
@app.route("/clothes")
def clothes():
    return render_template("ClotheHangers.html")


# render Clothe Lines & Racks
@app.route("/clothelines")
def clothelines():
    return render_template("ClotheLines.html")


# render Garbage & Recycling Bins
@app.route("/garbage")
def garbage():
    return render_template("Garbage.html")


# render Iron
@app.route("/ironingboard")
def ironingboard():
    return render_template("IronBoards.html")


# render Ironing Boards
@app.route("/ironingtools")
def ironingtools():
    return render_template("IroningTools.html")


# render Laundry Bags
@app.route("/laundrybags")
def laundrybags():
    return render_template("LaundryBags.html")


# render Wash Bags
@app.route("/washballs")
def washballs():
    return render_template("WashBalls.html")


# render Kitchen_and_Dining.html
@app.route("/kitchen_dining")
def kitchen_dining():
    return render_template("Kitchen_and_Dining.html")


# render Bakeware
@app.route("/bakeware")
def bakeware():
    return render_template("Bakeware.html")


# render Drinkware
@app.route("/drinkware")
def drinkware():
    return render_template("Drinkware.html")


# render Coffee & Tea
@app.route("/coffeetea")
def coffeetea():
    return render_template("CoffeeTea.html")


# render Colanders and Food Strainers
@app.route("/colander")
def colander():
    return render_template("Colanders.html")


# render Cookware
@app.route("/cookware")
def cookware():
    return render_template("Cookware.html")


# render Cutlery
@app.route("/cutlery")
def cutlery():
    return render_template("Cutlery.html")


# render Dinnerware
@app.route("/dinnerware")
def dinnerware():
    return render_template("Dinnerware.html")


# render Kitchen and Table Lenin
@app.route("/tablelenin")
def tablelenin():
    return render_template("TableLinen.html")


# render Kitchen Storage & Accessories
@app.route("/kitchenstorage")
def kitchenstorage():
    return render_template("KitchenStorage.html")


# render Kitchen Utensils
@app.route("/kitchenutensils")
def kitchenutensils():
    return render_template("KitchenUtensils.html")


# render Lighting.html
@app.route("/lighting")
def lighting():
    return render_template("Lighting.html")


# render Bathroom Lighting
@app.route("/bathroomlighting")
def bathroomlighting():
    return render_template("BathroomLighting.html")


# render Ceiling Lights
@app.route("/ceilinglights")
def ceilinglights():
    return render_template("CeilingLights.html")


# render Floor Lamps
@app.route("/floorlamps")
def floorlamps():
    return render_template("FloorLamps.html")


# render Lamp Shades
@app.route("/lampshades")
def lampshades():
    return render_template("LampShades.html")


# render LED Bulbs
@app.route("/led")
def led():
    return render_template("LEDBulbs.html")


# render Lighting Fixture & Components
@app.route("/lightingfixtures")
def lightingfixtures():
    return render_template("LightingFixtures.html")


# render Outdoor Lighting
@app.route("/outdoorlighting")
def outdoorlighting():
    return render_template("OutdoorLighting.html")


# render Specialty Lighting
@app.route("/specialtylighting")
def specialtylighting():
    return render_template("SpecialtyLighting.html")


# render Table Lamps
@app.route("/tablelamps")
def tablelamps():
    return render_template("TableLamps.html")


# render Wall Lights & Sconces
@app.route("/walllights")
def walllights():
    return render_template("WallLights.html")


# render Home_Decor.html
@app.route("/decor")
def decor():
    return render_template("Home_Decor.html")


# render Clock
@app.route("/clock")
def clock():
    return render_template("Clocks.html")


# render Aromatheraphy & Home Fragrance
@app.route("/aromatherapy")
def aromatherapy():
    return render_template("Aromatheraphy.html")


# render Wall Stickers & Decals
@app.route("/wallstickers")
def wallstickers():
    return render_template("WallStickers.html")


# render Cushions & Covers
@app.route("/cushions")
def cushions():
    return render_template("Cushions.html")


# render Decorative Bowls
@app.route("/decorativebowls")
def decorativebowls():
    return render_template("DecorativeBowls.html")


# render Mirrors
@app.route("/mirrors")
def mirrors():
    return render_template("Mirrors.html")


# render Pictures
@app.route("/pictures")
def pictures():
    return render_template("Pictures.html")


# render Window Treatment
@app.route("/windowtreatment")
def windowtreatment():
    return render_template("WindowTreatment.html")


# render Rugs & Carpets
@app.route("/rugs")
def rugs():
    return render_template("Rugs.html")


# render Seasonal
@app.route("/seasonal")
def seasonal():
    return render_template("Seasonal.html")


# render Veses and Vessels
@app.route("/veses")
def veses():
    return render_template("VesesVessels.html")


# render Wall Decor
@app.route("/walldecor")
def walldecor():
    return render_template("WallDecor.html")


# render Outdoor_and_Garden.html
@app.route("/outdoor_garden")
def outdoor_garden():
    return render_template("Outdoor_and_Garden.html")


# render Garden Decor & Ornaments
@app.route("/gardendecor")
def gardendecor():
    return render_template("GardenDecor.html")


# render Garden Soil & Fertilizers
@app.route("/gardensoil")
def gardensoil():
    return render_template("GardenSoil.html")


# render BBQ and Outdoor Dining
@app.route("/bbq")
def bbq():
    return render_template("BBQ.html")


# render Gardening Tools
@app.route("/gardentools")
def gardentools():
    return render_template("GardenningTools.html")


# render Plants, Seeds and Bulbs
@app.route("/plants")
def plants():
    return render_template("Plants.html")


# render Pots, Planter & Urns
@app.route("/pots")
def pots():
    return render_template("Pots.html")


# render Watering Systems & Garden Hoses
@app.route("/water")
def water():
    return render_template("WateringSystems.html")


# render Stationary_Craft.html
@app.route("/stationary_craft")
def stationary_craft():
    return render_template("Stationary_Craft.html")


# render Copier
@app.route("/copier")
def copier():
    return render_template("Copier.html")


# render Craft Supplies
@app.route("/craft")
def craft():
    return render_template("CraftSupplies.html")


# render Art Supplies
@app.route("/artsupplies")
def artsupplies():
    return render_template("ArtSupplies.html")


# render Gift and Wrapping
@app.route("/gift")
def gift():
    return render_template("Gift.html")


# render School Sets
@app.route("/school")
def school():
    return render_template("SchoolSets.html")


# render Packaging and Cartoons
@app.route("/packaging")
def packaging():
    return render_template("Packaging.html")


# render Paper Products
@app.route("/paperproducts")
def paperproducts():
    return render_template("PaperProducts.html")


# render School and Office Equipment
@app.route("/schooloffice")
def schooloffice():
    return render_template("SchoolOffice.html")


# render Shipping Bags
@app.route("/shippingbags")
def shippingbags():
    return render_template("ShippingBags.html")


# render Sewing
@app.route("/sewing")
def sewing():
    return render_template("Sewing.html")


# render Writing and Correction
@app.route("/writingcorrection")
def writingcorrection():
    return render_template("WritingCorrection.html")


# render Tools_Home_Improvement.html
@app.route("/tools_home")
def tools_home():
    return render_template("Tools_Home_Improvement.html")


# render Electrical
@app.route("/electrical")
def electrical():
    return render_template("Electrical.html")


# render Fixtures and Plumbing
@app.route("/fixtures")
def fixtures():
    return render_template("Plumbing.html")


# render Hand Tools
@app.route("/handtools")
def handtools():
    return render_template("HandTools.html")


# render Hardware
@app.route("/hardware")
def hardware():
    return render_template("Hardware.html")


# render Measuring & Leveling
@app.route("/measuringleveling")
def measuringleveling():
    return render_template("MeasuringLeveling.html")


# render Paint, Wallpaper & Flooring
@app.route("/paint")
def paint():
    return render_template("Paint.html")


# render Power Tools
@app.route("/powertools")
def powertools():
    return render_template("PowerTools.html")


# render Protective Clothing and Equipment
@app.route("/ppe")
def ppe():
    return render_template("PPE.html")


# render Safety
@app.route("/safety")
def safety():
    return render_template("Safety.html")


# render Work Lights
@app.route("/worklights")
def worklights():
    return render_template("WorkLights.html")


# calls the registration.html
@app.route("/register")
def register():
    return render_template("registration.html", remark="")


# retrieves the data from registration form
@app.route("/register_account", methods=["POST"])
def registerAccount():
    if "deny" in request.form['flag']:
        return render_template("registration.html", remark="Password Mismatch!")
    data: dict = {
        "lastname": request.form['lastname'],
        "firstname": request.form['firstname'],
        "email": request.form['email'],
        "contact": request.form['number'],
        "password": request.form['password']
    }
    register_account(randint(0, 19999), data['lastname'], data['firstname'], data['email'], data['contact'],
                     hashString(data['password']))
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
