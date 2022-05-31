from flask import Flask, redirect, url_for, render_template, request, session
from database import register_account, hashString, getAccount
import database
import utility
from random import randint

app = Flask(__name__)
app.secret_key = '39cm85yu234m98'


# go to landing page
@app.route("/")
def landing_page():
    return render_template("Navigation/LandingPage.html")


@app.route("/home")
def home():
    return render_template("Navigation/LandingPage.html", account=session['username'])


# calls the login.html, asks the user to enter email and password
@app.route("/login")
def login():
    return render_template("Navigation/Login.html")


# retrieves data from login form, check if account exist in database
@app.route("/login_account", methods=['POST'])
def loginAccount():
    print(hashString(request.form["psw"]))
    if getAccount(request.form["email"], hashString(request.form["psw"])):
        session['username'] = request.form["email"]
        return render_template("LandingPage.html", account=session['username'])
    else:
        return "invalid"


# render bathrobes
@app.route("/productListing/<prod>")
def productListing(prod: int):
    DATA: list = []
    data: utility.Product = database.getProduct(prod)
    DATA.append(data)
    INFO: list = []
    data: utility.ProductInfo = database.getProductInfo(prod)
    INFO.append(data)

    return render_template("Listing/item.html", data=DATA, info=INFO,
                           category=utility.parseCatLocation(INFO[0].category),
                           sub_category=utility.parseSubCatLocation(prod),
                           account=session['username'])


@app.route("/bath")
def bath():
    return render_template("Categories/bath.html", account=session['username'])


# render product
@app.route("/product/<items>")
def showProduct(items: str):
    CODES: list = items.split("...")
    m: int = int(CODES[0])
    r: int = int(CODES[1])
    DATA: list = []
    for x in range(m, r):
        data: utility.Product = database.getProduct(x)
        DATA.append(data)
    INFO: list = []
    for x in range(m, r):
        data: utility.ProductInfo = database.getProductInfo(x)
        INFO.append(data)
    return render_template("ProductInfo/PRODUCT_INFORMATION.html", data=DATA, info=INFO,
                           category=utility.parseCatLocation(INFO[0].category),
                           account=session['username'])


# render bath mats
@app.route("/bathmats")
def bathmats():
    return redirect("/product/101...106")


# render towel
@app.route("/towel")
def towel():
    return redirect("/product/201...206")


# render bathrobes
@app.route("/bathrobes")
def bathrobes():
    return redirect("/product/301...306")


# render bath mirrors
@app.route("/bathmirrors")
def bathmirrors():
    return redirect("/product/601...606")


# render Linen Towers & Cabinets
@app.route("/linentowers")
def linentowers():
    return redirect("/product/901...906")


# render Towel Rails & Warmers
@app.route("/towelrails")
def towelrails():
    return redirect("/product/1201...1206")


# render Bathroom Counter Storage
@app.route("/bathroomcounter")
def bathroomcounter():
    return redirect("/product/401...406")


# render Holders & Dispensers
@app.route("/holders")
def holders():
    return redirect("/product/501...506")


# render Shower Curtains & Accessories
@app.route("/showercurtains")
def showercurtains():
    return redirect("/product/1001...1006")


# render Shower Caddies & Hangers
@app.route("/showerhangers")
def showerhangers():
    return redirect("/product/1101...1106")


# render Bathroom Shelving
@app.route("/bathroomshelving")
def bathroomshelving():
    return redirect("/product/801...806")


# render Bathroom Scale
@app.route("/bathroomscale")
def bathroomscale():
    return redirect("/product/701...706")


# render Bedding.html
@app.route("/bedding")
def bedding():
    return render_template("Categories/Bedding.html", account=session['username'])


# render Bedding Runners & Skirts
@app.route("/bedrunners")
def bedrunners():
    return redirect("/product/1301...1306")


# render Bed Sheet
@app.route("/bedsheet")
def bedsheet():
    return redirect("/product/1401...1406")


# render Blankets & Throws
@app.route("/blanket")
def blanket():
    return redirect("/product/1501...1506")


# render Comforters, Quilts & Duvets
@app.route("/comforter")
def comforter():
    return redirect("/product/1601...1606")


# render Electric Blanket
@app.route("/electricblanket")
def electricblanket():
    return redirect("/product/1701...1706")


# render Mattress Pads
@app.route("/mattresspads")
def mattrespads():
    return redirect("/product/1801...1806")


# render Pillow Cases
@app.route("/pillowcases")
def pillowcases():
    return redirect("/product/1901...1906")


# render Pillow Protectors
@app.route("/pillowprotectors")
def pillowprotectors():
    return redirect("/product/2001...2006")


# render Pillow Bolsters
@app.route("/pillowbolsters")
def pillowbolsters():
    return redirect("/product/2101...2106")


# render Furniture.html
@app.route("/furniture")
def furniture():
    return render_template("Categories/Furniture.html", account=session['username'])


# render Bedroom Furniture
@app.route("/bedroomfurniture")
def bedroomfurniture():
    return redirect("/product/2201...2206")


# render Chairs
@app.route("/chairs")
def chair():
    return redirect("/product/2301...2306")


# render Gaming Furniture
@app.route("/gamingfurniture")
def gamingfurniture():
    return redirect("/product/2401...2406")


# render Home Office Furniture
@app.route("/officefurniture")
def officefurniture():
    return redirect("/product/2501...2506")


# render Kids Tables & Sets
@app.route("/kidstable")
def kidstable():
    return redirect("/product/2601...2606")


# render Kitchen & Dining Furniture
@app.route("/kithcenfurniture")
def kithcenfurniture():
    return redirect("/product/2701...2706")


# render Living Room Furniture
@app.route("/livingroom")
def livingroom():
    return redirect("/product/2801...2806")


# render Mattress
@app.route("/mattress")
def mattress():
    return redirect("/product/2901...2906")


# render Media or TV Storge
@app.route("/mediastorage")
def mediastorage():
    return redirect("/product/3001...3006")


# render Outdoor Furniture
@app.route("/outdoorfurniture")
def outdoorfurniture():
    return redirect("/product/3101...3106")


# render Sofas
@app.route("/sofas")
def sofas():
    return redirect("/product/3201...3206")


# render Wardrobes
@app.route("/wardrobe")
def wardrobe():
    return redirect("/product/3301...3306")


# render Storage_and_Organization.html
@app.route("/storage")
def storage():
    return render_template("Categories/Storage_and_Organization.html", account=session['username'])


# render Compression Bags
@app.route("/compressionbags")
def compressionbags():
    return redirect("/product/3401...3406")


# render Deck Boxes & Balcony Storage
@app.route("/deckboxes")
def deckboxes():
    return redirect("/product/3501...3506")


# render Medicine & First Ais Storage
@app.route("/medicine")
def medicine():
    return redirect("/product/3701...3706")


# render Shoe Organiser
@app.route("/shoe")
def shoe():
    return redirect("/product/3801...3806")


# render Space Savers
@app.route("/spacesavers")
def spacesavers():
    return redirect("/product/3901...3906")


# render Storge Bins & Baskets
@app.route("/storagebins")
def storagebins():
    return redirect("/product/4001...4006")


# render Wardrobe Organiser
@app.route("/wardrobeorganiser")
def wardrobeorganiser():
    return redirect("/product/4101...4106")


# render Laundry_and_Cleaning_Equipment.html
@app.route("/laundry_cleaning")
def laundry_cleaning():
    return render_template("Categories/Laundry_and_Cleaning_Equipment.html", account=session['username'])


# render Brooms., Mops & Sweepers
@app.route("/brooms")
def brooms():
    return redirect("/product/4201...4206")


# render Cleaning Buckets & Tubs
@app.route("/cleaning")
def cleaning():
    return redirect("/product/4301...4306")


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
    return render_template("Categories/Kitchen_and_Dining.html", account=session['username'])


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
    return render_template("Categories/Lighting.html", account=session['username'])


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
    return render_template("Categories/Home_Decor.html", account=session['username'])


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
    return render_template("Categories/Outdoor_and_Garden.html", account=session['username'])


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
    return render_template("Categories/Stationary_Craft.html", account=session['username'])


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
    return render_template("Categories/Tools_Home_Improvement.html", account=session['username'])


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
    return render_template("Navigation/registration.html", remark="")


# retrieves the data from registration form
@app.route("/register_account", methods=["POST"])
def registerAccount():
    if "deny" in request.form['flag']:
        return render_template("Navigation/registration.html", remark="Password Mismatch!")
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
