
# Payload

# Video Upload
# Metadata: Title, Description, Tags

import boto3
import botocore
import logging
import json

logger = logging.getLogger()



class StateMachine:
    """Encapsulates Step Functions state machine actions."""
    def __init__(self, stepfunctions_client):
        """
        :param stepfunctions_client: A Boto3 Step Functions client.
        """
        self.stepfunctions_client = stepfunctions_client

    def start(self, state_machine_arn, run_input):
        """
        Start a run of a state machine with a specified input. A run is also known
        as an "execution" in Step Functions.

        :param state_machine_arn: The ARN of the state machine to run.
        :param run_input: The input to the state machine, in JSON format.
        :return: The ARN of the run. This can be used to get information about the run,
                 including its current status and final output.
        """
        try:
            response = self.stepfunctions_client.start_execution(
                stateMachineArn=state_machine_arn, input=run_input)
        except botocore.exceptions.ClientError as err:
            logger.error(
                "Couldn't start state machine %s. Here's why: %s: %s", state_machine_arn,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return response['executionArn']


def lambda_handler(event, context):
    # TODO implement
    stepfunctions_client = boto3.client('stepfunctions')
    state_machine = StateMachine(stepfunctions_client)

    state_machine_arn = 'arn:aws:states:us-east-1:822767915126:stateMachine:Netflix_For_Me_NFLX'
    payload = json.dumps({
        "hello": "world"
    })
    state_machine.start(state_machine_arn=state_machine_arn, run_input=payload)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


lambda_handler()