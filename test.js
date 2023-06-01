/* var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var db = null
MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("WT_Project");
  var myobj = { name: "Company Inc", address: "Highway 37" };
  dbo.collection("Users").insertOne(myobj, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
}); */

const mongoose = require("mongoose");


mongoose.connect("mongodb://localhost:27017/WT_Project",{
    useNewUrlParser: true,
    useUnifiedTopology:true

})

.then(()=>console.log("Connected"))
.catch((error)=>console.log(error));