import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apiGateway from "aws-cdk-lib/aws-apigateway";
import { compileFunction } from 'vm'; 
import { Compatibility } from 'aws-cdk-lib/aws-ecs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class BrandingInfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    const layer = new lambda.LayerVersion(this, "BaseLayer", {
      code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
    });

    const apiLambda = new lambda.Function(this, "ApiFunction",{
      runtime:lambda.Runtime.PYTHON_3_9,
      code:lambda.Code.fromAsset("../app/"),
      handler : "api.handler",
      layers:[layer],

      
    });

    const Api = new apiGateway.RestApi(this, "RestApi", {
      restApiName: "Tutorial API",
  });
  Api.root.addProxy({
    defaultIntegration: new apiGateway.LambdaIntegration(apiLambda),
  });

}
}