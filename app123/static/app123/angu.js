

app = angular.module('demoapp', ['ngRoute']);

// app = angular.module('demoapp', []);

app.controller('DemoCtrl', ['$scope', function($scope) {
    $scope.num = 222;
	console.log("inside first controller....");
    $scope.save = function() {
      $(".data").html("Click: " + $scope.num);
      $scope.num += 1;
    };
}]);

app.controller('restctrl', function($scope, $http) {
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



app.config(function($routeProvider,$locationProvider) {
    $routeProvider
        .when('/app123/viewindoor', {
			//console.log("xxxxxxxxxxx")
            templateUrl: '/static/app123/viewindoor.html',
            //controller: 'FirstController'
        })
        .when('/app123/viewoutdoor', {
            templateUrl: '/static/app123/viewoutdoor.html',
           // controller: 'SecondController'
        })
		 .when('/app123/adddood', {
            templateUrl: '/static/app123/viewadddood.html',
           // controller: 'SecondController'
        })
        .otherwise({
            redirectTo: '/app123/'
			//console.log("yyyyyyyyyyyy");
        });
		// $locationProvider.html5Mode(true);
		console.log("zzzzzzzzzzzz989898");
});




/* angularjs for adding review etc.*/

// appreview = angular.module('demoreview', []);

app.controller('contreview', function($scope) {
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


app.controller('adddood', function($scope) {
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

app.controller('DemoCtrl123', ['$scope', function($scope) {
    
	
  $scope.dummy="dummy123";
  console.log("inside amazon s3 controller....");
  $scope.sizeLimit      = 10585760; // 10MB in Bytes
  $scope.uploadProgress = 0;
$scope.creds={} ;

$scope.creds.bucket='';
$scope.creds.access_key='';
$scope.creds.secret_key='';

console.log($scope.creds.bucket);
console.log($scope.creds.access_key);
console.log($scope.creds.secret_key);


  $scope.upload = function() {
	   console.log("inside amazon s3 controller upload function....");
    AWS.config.update({ accessKeyId: $scope.creds.access_key, secretAccessKey: $scope.creds.secret_key });
    AWS.config.region = 'us-west-2';
    var bucket = new AWS.S3({ params: { Bucket: $scope.creds.bucket } });
    console.log($scope.creds.bucket);
	console.log(bucket);
    if($scope.file) {
        // Perform File Size Check First
        /*var fileSize = Math.round(parseInt($scope.file.size));
		console.log(filesize);
        if (fileSize > $scope.sizeLimit) {
          toastr.error('Sorry, your attachment is too big. <br/> Maximum '  + $scope.fileSizeLabel() + ' file attachment allowed','File Too Large');
          return false;
        }*/
		
        // Prepend Unique String To Prevent Overwrites
        var uniqueFileName = $scope.uniqueString() + '-' + $scope.file.name;
        
        // var params = { Key: uniqueFileName, ContentType: $scope.file.type, Body: $scope.file, ServerSideEncryption: 'AES256' };
         var params = { Key: uniqueFileName, ContentType: $scope.file.type, Body: $scope.file};
		console.log(params);
		console.log(uniqueFileName);
		console.log($scope.file.type);
		console.log($scope.file);
					
        bucket.putObject(params, function(err, data) {
          if(err) {
			console.log("inside amazon s3 controller putobject error....");
            toastr.error(err.message,err.code);
            return false;
          }
          else {
            // Upload Successfully Finished
			console.log("inside amazon s3 controller upload succesful....");
            toastr.success('File Uploaded Successfully', 'Done');

            // Reset The Progress Bar
            setTimeout(function() {
              $scope.uploadProgress = 0;
              $scope.$digest();
            }, 4000);
          }
        })
        .on('httpUploadProgress',function(progress) {
          $scope.uploadProgress = Math.round(progress.loaded / progress.total * 100);
          $scope.$digest();
        });
      }
      else {
        // No File Selected
        toastr.error('Please select a file to upload');
      }
    }

    $scope.fileSizeLabel = function() {
    // Convert Bytes To MB
    return Math.round($scope.sizeLimit / 1024 / 1024) + 'MB';
  };

  $scope.uniqueString = function() {
    var text     = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 8; i++ ) {
      text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
  }
	
}]);


app.directive('file', function() {
  return {
    restrict: 'AE',
    scope: {
      file: '@'
    },
    link: function(scope, el, attrs){
      el.bind('change', function(event){
        var files = event.target.files;
        var file = files[0];
        scope.file = file;
        scope.$parent.file = file;
        scope.$apply();
      });
    }
	
  };
});








