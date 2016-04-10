

// app123 = angular.module('demoapp', ['ngRoute']);

app123 = angular.module('demoapp', []);

app123.controller('DemoCtrl', ['$scope', function($scope) {
    $scope.num = 222;
	console.log("inside first controller....");
    $scope.save = function() {
      $(".data").html("Click: " + $scope.num);
      $scope.num += 1;
    };
}]);

app123.controller('restctrl', function($scope, $http) {
	console.log("1111111555555")
  $http({
    method : "GET",
    url : "http://localhost:8000/app123/api/"
  }).then(function mySucces(response) {
      // $scope.myWelcome = response.data;
	  console.log("2222222222229999")
	  $scope.myWelcome2 = "ccc";
	  $scope.myWelcome3 =response.data;
	  console.log($scope.myWelcome2)
	  console.log($scope.myWelcome3)
    }, function myError(response) {
     // $scope.myWelcome = response.statusText;
	 $scope.myWelcome = "zzzzzzz121212";
	   console.log("33333333333999999999")
  });
  
  $scope.myWelcome = "0000000000000000";
});

/* 
app.controller('restctrl', function($scope) {
  
  $scope.num = 4444;
    $scope.save = function() {
      $(".data2").html("Click: " + $scope.num);
      $scope.num += 1;
    };
});*/


/*
app.config(function($routeProvider,$locationProvider) {
    $routeProvider
        .when('/app123/viewindoor', {
			//console.log("xxxxxxxxxxx")
            templateUrl: '/static/app123/viewindoor.html',
            //controller: 'FirstController'
        })
        .when('/viewoutdoor', {
            templateUrl: 'viewoutdoor.html',
           // controller: 'SecondController'
        })
        .otherwise({
            redirectTo: '/app123/'
			//console.log("yyyyyyyyyyyy");
        });
		$locationProvider.html5Mode(true);
		console.log("zzzzzzzzzzzz989898");
});


*/

/* angularjs for adding review etc.*/

// appreview = angular.module('demoreview', []);

app123.controller('contreview', function($scope) {
	console.log("zzzzzzzzzzzz989898");
    $scope.addreview = function() {
        $scope.dummy="it works";
		$scope.indicator="1";
		 $scope.showbutton="true";
		console.log("inside review controller111....")
    };
	
	  $scope.toshow = function() {
		
		if ($scope.indicator == 1)
                 return true;
                   else 
                return false;
		
		console.log("inside review controller222....")
    };
	
	
	
	
});










