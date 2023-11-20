# LoremIpsumAPI
A simple API that generates Lorem Ipsum Text


TO request data from the Microservice:

Endpoint: THE endpoint of the API is '/generate-text'. This is what generates the lorem ipsum text.

Currently it is being hosted locally, so to access the API it is done via a GET requested. 
If hosted locally, the URL will be something like this: 'http//localhost:5000/generate-text'

So, the api also accepts a 'size' parameter, which the size parameter is specifically for the number of lines of lorem ipsum that will generate.
If it isn't provided it will default to 1

EXAMPLE CALL:

GET http://localhost:5000/generate-text?size=3

BASH:

curl localhost:5000/generate-text?size=3


TO receive data from the Microservice:

The API responds with a JSON object. IT has the key 'text' which will hold the generateed lorem upsum text

Example Response:

{
  "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In non lacinia est. Maecenas elit sem, fringilla eget velit sit amet, viverra elementum ex. Morbi a augue finibus, tempus nisl eu, tincidunt nisl. Sed accumsan magna ligula, vel venenatis quam finibus in. Proin pretium accumsan elit, ac sagittis nibh gravida in. Suspendisse vitae orci vitae augue tempus malesuada. Sed lacinia magna eu quam porttitor, quis auctor lorem imperdiet. Integer dapibus congue metus ornare bibendum. Sed eleifend tempus massa ac convallis. Sed viverra, quam et imperdiet interdum, nisi ligula laoreet lorem, eu luctus ex magna eget augue. Vivamus consectetur luctus euismod"
}




![Blank diagram](https://github.com/Heyzppl/LoremIpsumAPI/assets/104742994/267c3df2-ff54-4be3-816c-5e916dc53a8e)

