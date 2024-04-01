using Itinero; 
using Itinero.IO.Osm;
using Itinero.Osm.Vehicles;

var routerDb = new RouterDb();
var profile = Vehicle.Car.Fastest(); // the default OSM car profile.

  using (var stream = new FileInfo("quebec-latest.osm.pbf").OpenRead())
  {
      // create the network for cars.
      routerDb.LoadOsmData(stream, Vehicle.Car);
  }

  // write the routerdb to disk.
  using (var stream = new FileInfo(@"quebec.routerdb").Open(FileMode.Create))
  {
      routerDb.Serialize(stream);
  }