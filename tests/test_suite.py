import unittest
from typing import Dict, Any
from distributed_lock_manager.lock_manager import LockManagerEngine, LockManagerContext, LockManagerConfig
from distributed_lock_manager.fencing_tokens import FencingTokensEngine, FencingTokensContext, FencingTokensConfig
from distributed_lock_manager.lease_renewers import LeaseRenewersEngine, LeaseRenewersContext, LeaseRenewersConfig
from distributed_lock_manager.backend_stores import BackendStoresEngine, BackendStoresContext, BackendStoresConfig
from distributed_lock_manager.deadlock_detectors import DeadlockDetectorsEngine, DeadlockDetectorsContext, DeadlockDetectorsConfig
from distributed_lock_manager.telemetry_metrics import TelemetryMetricsEngine, TelemetryMetricsContext, TelemetryMetricsConfig

class ComprehensiveTestSuite(unittest.TestCase):
    def test_lock_manager_basic_lifecycle(self):
        engine = LockManagerEngine()
        ctx = LockManagerContext(correlation_id='cid-lock_manager-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_fencing_tokens_basic_lifecycle(self):
        engine = FencingTokensEngine()
        ctx = FencingTokensContext(correlation_id='cid-fencing_tokens-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_lease_renewers_basic_lifecycle(self):
        engine = LeaseRenewersEngine()
        ctx = LeaseRenewersContext(correlation_id='cid-lease_renewers-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_backend_stores_basic_lifecycle(self):
        engine = BackendStoresEngine()
        ctx = BackendStoresContext(correlation_id='cid-backend_stores-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_deadlock_detectors_basic_lifecycle(self):
        engine = DeadlockDetectorsEngine()
        ctx = DeadlockDetectorsContext(correlation_id='cid-deadlock_detectors-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_telemetry_metrics_basic_lifecycle(self):
        engine = TelemetryMetricsEngine()
        ctx = TelemetryMetricsContext(correlation_id='cid-telemetry_metrics-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

