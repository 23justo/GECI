app = angular.module('contable', []);

app.controller(
    
    
    'MovimientoCita',['$scope','$http',function($scope,$http){
        $scope.movimientos;
        $scope.movimiento_data = null;
        $scope.movimiento_data_toggle = false;

        $scope.obtenermovimientos = function(){
            $http.get('/movimientocita/api-ObtenerMovimientos').success(function(data){
                $scope.movimientos = angular.fromJson(data);
            }).error(function(err){
            });
        };

        $scope.obtenermovimientos_data = function(pk){
            $scope.movimiento_data = pk;
            $scope.movimiento_data_toggle = true;
            $http.get('/movimientocita/api-ObtenerMovimientoEspecifico/'+pk).success(function(data){
                $scope.movimiento_data = angular.fromJson(data);
                console.log($scope.movimiento_data);
            }).error(function(err){
            });
        };

        $scope.search = function (item) {
            if ($scope.searchText == undefined) {
                return true;
            }
            else {
                if (item.doctor.toLowerCase().indexOf($scope.searchText.toLowerCase()) != -1 ||
                    item.paciente.toLowerCase().indexOf($scope.searchText.toLowerCase()) != -1 ||
                    item.fecha.toLowerCase().indexOf($scope.searchText.toLowerCase()) != -1
                    ) {
                    return true;
                }
            }
            return false;
        };
        

        var init = function () {
            $scope.obtenermovimientos();
         };
         
         init();
}]);