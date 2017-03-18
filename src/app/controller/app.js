var app = angular.module('apps', ['ngAnimate', 'ngSanitize', 'ngRoute', 'ui.bootstrap'])

app.config(function($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'src/app/templates/home/home.html',
		controller : "homeCrl"
	})
	.when('/profile', {
		templateUrl: 'src/app/templates/profile/profile.html',
		controller : "profileCtrl"
	})
	.when('/login', {
		templateUrl: 'src/app/templates/account/login.html',
		controller : "loginCtrl",
	})
	.when('/signup', {
		templateUrl: 'src/app/templates/account/signup.html',
		controller : "signupCtrl"
	})
	.when('/detail', {
		templateUrl: 'src/app/templates/home/detail/detail.html',
		controller : "detailCtrl"
	})
})
.directive('fileInput', ['$parse', function ($parse) {
	return {
		restrict: 'A',
		link: function (scope, element, attributes) {
			element.bind('change', function () {
				$parse(attributes.fileInput)
				.assign(scope,element[0].files)
				scope.$apply()
			});
		}
	};
}]);
;

// controller

app.controller("signupCtrl", ['$location','$scope', '$http', function($location, $scope, $http){
	console.log('signup')

	$scope.data = { 
		gender : '1',
	}

	$scope.Signup = function(){
		console.log('11111111')
		var data = $scope.data;

		var url_signup = '/signup?username='+data.username + "&password="+data.password+"&email="+data.email+"&gender=" + data.gender;
		console.log(url_signup)
		$http.get(url_signup).then(function(response){
			console.log(response.data)
			if(response.data.result>0){
				$location.path('/login');
			}
		})		
	}
}])

app.controller("loginCtrl", ['$rootScope', '$location', '$scope', '$http', function($rootScope, $location, $scope, $http, AUTH_EVENTS, AuthService){
	console.log('login')

	$scope.Login = function(){
		var data = $scope.data;
		var fd = new FormData();
		fd.append('username', data.username)
		fd.append('password', data.password)
		var url_login = '/login';
		$http.post(url_login, fd, {
			headers: {
				'Content-Type': undefined,
			},
			transformRequest: angular.identity
		}).then(function(response){
			console.log(response.data)
			if(response.data.result > 0){
				checkUser =true;
				console.log(checkUser)
				$location.path('/')
			}
		})
	}
}])


app.controller("homeCrl", ['$scope', '$http', '$log', function($scope, $http, $log){
	// rating
	$scope.rate = 0;
	$scope.max = 5;

	$scope.getRate = function(rate){
		console.log(rate)
	}

	$scope.currentPage = 1;
	function listBlog(){
		var url_list = '/list-all-blog?page=' + $scope.currentPage+ '&total='+10;
		$http.get(url_list).then(function(response){
			$scope.listBlog = response.data.data;
			$scope.totalItems = response.data.totalItems;
		});
	}
	
	listBlog();

	$scope.goToPage = function(currentPage) {
		$scope.currentPage = currentPage;
		listBlog();
	};

	$scope.showModal = false;
	$scope.openFromAdd = function(){
		$scope.showModal = !$scope.showModal;
	};

	$scope.addBlog = function(data,files){
		var fd = new FormData();
		fd.append('title', data.title);
		fd.append('content', data.content);
		fd.append('file', files[0]);
		console.log(fd)
		var url_add = '/home/add-blog';
		$http.post(url_add, fd, {
			headers: {
				'Content-Type': undefined,
			},
			transformRequest: angular.identity
		}).then(function(response){
			if(response.data.result > 0){
				$('#title').val("");
				$('#content').val("");
				$('#file').val(null);
				$('.modal-open .modal').modal('hide');
				listBlog();
			}
		})
	}

	$scope.change = function(data){
		console.log(data)
		var url_search = '/search?search='+data;
		$http.get(url_search).then(function(response){
			console.log(response)
			if(response.data.result > 0){
				console.log('9999999999')
				$scope.listBlog = response.data.data
			}
		})
	}

}])

app.controller("detailCtrl", ['$location', '$filter', '$routeParams', '$scope', '$http', function($location, $filter, $routeParams, $scope, $http){
	console.log('detail')
	function detail(){
		var url_detail = '/detail-blog?id='+$routeParams.id;
		$http.get(url_detail).then(function(response){
			$scope.data = response.data.data;
			$scope.data.updated = $filter('date')(response.data.data.updated, 'medium')
		});
	}
	
	detail();

	$scope.showModal = false;
	$scope.openFromEdit = function(){
		$scope.showModal = !$scope.showModal;
	};

	$scope.showModalDelete = false;
	$scope.openAlertDelete = function(){
		console.log('Form delete')
		$scope.showModalDelete = !$scope.showModalDelete;
	}

	$scope.imageUpload = function(element){
		var reader = new FileReader();
		reader.onload = $scope.imageIsLoaded;
		reader.readAsDataURL(element.files[0]);
	}

	$scope.imageIsLoaded = function(e){
		$scope.$apply(function() {
			$scope.stepsModel = e.target.result;
			$('#img1').css('display', 'none');
			$('#img2').css('display', 'block');
		});
	}

	$scope.uploadFile = function(files){
		console.log('777777777')
		console.log(files[0])
	}

	// edit
	$scope.save = function(data, files){
		console.log('edit')
		var fd = new FormData();
		fd.append('id', $routeParams.id);
		fd.append('title', data.title);
		fd.append('content', data.content);
		fd.append('file', files[0]);
		var url_edit = '/detail-blog/edit-blog';
		console.log(url_edit)
		$http.post(url_edit, fd, {
			headers: {
				'Content-Type': undefined,
			},
			transformRequest: angular.identity
		}).then(function(response){
			if(response.data.result > 0){
				$('.modal-open .modal').modal('hide');
				detail();
			}
		})
	}

	$scope.yes = function(){
		console.log('YES')
		var fd = new FormData();
		var url_del = '/detail-blog/delete';
		fd.append('id', $routeParams.id)
		$http.post(url_del, fd, {
			headers: {
				'Content-Type': undefined,
			},
			transformRequest: angular.identity
		}).then(function(response){
			if(response.data.result > 0){
				$('.modal-open .modal').modal('hide');
				setTimeout(function(){ 
					$location.url('/'); 
				}, 100);
			}
		})
	}
	$scope.no = function(){
		console.log('NO')
		$('.modal-open .modal').modal('hide');
	}

}]);

app.controller("profileCtrl", ['$scope', '$http', function($scope, $http){
	console.log('profile')

}])


app.directive('modal', function () {
	return {
		template: '<div class="modal fade">' + 
		'<div class="modal-dialog">' + 
		'<div class="modal-content">' + 
		'<div class="modal-header">' + 
		'<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' + 
		'<h4 class="modal-title">{{title}}</h4>' + 
		'</div>' + 
		'<div class="modal-body" ng-transclude></div>' + 
		'</div>' + 
		'</div>' + 
		'</div>',
		restrict: 'E',
		transclude: true,
		replace:true,
		scope:true,
		link: function postLink(scope, element, attrs) {
			scope.title = attrs.title;

			scope.$watch(attrs.visible, function(value){
				if(value == true)
					$(element).modal('show');
				else
					$(element).modal('hide');
			});

			$(element).on('shown.bs.modal', function(){
				scope.$apply(function(){
					scope.$parent[attrs.visible] = true;
				});
			});

			$(element).on('hidden.bs.modal', function(){
				scope.$apply(function(){
					scope.$parent[attrs.visible] = false;
				});
			});
		}
	};
});