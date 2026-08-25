from client import PrivateEnterpriseContextCodeAutocompletionClient

def main():
    client = PrivateEnterpriseContextCodeAutocompletionClient()
    res = client.predict_multi_line_code_completion('def verify_jwt_signature_rsa256(token, public_key_pem):', True)
    print('Completion ID: ' + res['completion_id'] + ' (Latency: ' + str(res['prediction_latency_ms']) + 'ms)')
    print('Air-Gapped: ' + str(res['air_gapped_isolated']) + ' | Acceptance Score: ' + str(res['acceptance_probability_score_pct']) + '%')
    print('Predicted Code:')
    print(res['predicted_code_block'])

if __name__ == '__main__':
    main()
