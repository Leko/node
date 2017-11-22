# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_DOUBLE_ARRAY_TYPE",
  149: "FILLER_TYPE",
  150: "ACCESSOR_INFO_TYPE",
  151: "ACCESSOR_PAIR_TYPE",
  152: "ACCESS_CHECK_INFO_TYPE",
  153: "INTERCEPTOR_INFO_TYPE",
  154: "FUNCTION_TEMPLATE_INFO_TYPE",
  155: "OBJECT_TEMPLATE_INFO_TYPE",
  156: "ALLOCATION_SITE_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "SCRIPT_TYPE",
  159: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  160: "PROMISE_RESOLVE_THENABLE_JOB_INFO_TYPE",
  161: "PROMISE_REACTION_JOB_INFO_TYPE",
  162: "DEBUG_INFO_TYPE",
  163: "STACK_FRAME_INFO_TYPE",
  164: "PROTOTYPE_INFO_TYPE",
  165: "TUPLE2_TYPE",
  166: "TUPLE3_TYPE",
  167: "CONTEXT_EXTENSION_TYPE",
  168: "MODULE_TYPE",
  169: "MODULE_INFO_ENTRY_TYPE",
  170: "ASYNC_GENERATOR_REQUEST_TYPE",
  171: "FIXED_ARRAY_TYPE",
  172: "HASH_TABLE_TYPE",
  173: "FEEDBACK_VECTOR_TYPE",
  174: "TRANSITION_ARRAY_TYPE",
  175: "PROPERTY_ARRAY_TYPE",
  176: "SHARED_FUNCTION_INFO_TYPE",
  177: "CELL_TYPE",
  178: "WEAK_CELL_TYPE",
  179: "PROPERTY_CELL_TYPE",
  180: "SMALL_ORDERED_HASH_MAP_TYPE",
  181: "SMALL_ORDERED_HASH_SET_TYPE",
  182: "CODE_DATA_CONTAINER_TYPE",
  183: "JS_PROXY_TYPE",
  184: "JS_GLOBAL_OBJECT_TYPE",
  185: "JS_GLOBAL_PROXY_TYPE",
  186: "JS_MODULE_NAMESPACE_TYPE",
  187: "JS_SPECIAL_API_OBJECT_TYPE",
  188: "JS_VALUE_TYPE",
  189: "JS_MESSAGE_OBJECT_TYPE",
  190: "JS_DATE_TYPE",
  191: "JS_API_OBJECT_TYPE",
  192: "JS_OBJECT_TYPE",
  193: "JS_ARGUMENTS_TYPE",
  194: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  195: "JS_GENERATOR_OBJECT_TYPE",
  196: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  197: "JS_ARRAY_TYPE",
  198: "JS_ARRAY_BUFFER_TYPE",
  199: "JS_TYPED_ARRAY_TYPE",
  200: "JS_DATA_VIEW_TYPE",
  201: "JS_SET_TYPE",
  202: "JS_MAP_TYPE",
  203: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  204: "JS_SET_VALUE_ITERATOR_TYPE",
  205: "JS_MAP_KEY_ITERATOR_TYPE",
  206: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  207: "JS_MAP_VALUE_ITERATOR_TYPE",
  208: "JS_WEAK_MAP_TYPE",
  209: "JS_WEAK_SET_TYPE",
  210: "JS_PROMISE_TYPE",
  211: "JS_REGEXP_TYPE",
  212: "JS_ERROR_TYPE",
  213: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  214: "JS_STRING_ITERATOR_TYPE",
  215: "JS_TYPED_ARRAY_KEY_ITERATOR_TYPE",
  216: "JS_FAST_ARRAY_KEY_ITERATOR_TYPE",
  217: "JS_GENERIC_ARRAY_KEY_ITERATOR_TYPE",
  218: "JS_UINT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  219: "JS_INT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  220: "JS_UINT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  221: "JS_INT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  222: "JS_UINT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  223: "JS_INT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  224: "JS_FLOAT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  225: "JS_FLOAT64_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  226: "JS_UINT8_CLAMPED_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  227: "JS_FAST_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  228: "JS_FAST_HOLEY_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  229: "JS_FAST_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  230: "JS_FAST_HOLEY_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  231: "JS_FAST_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  232: "JS_FAST_HOLEY_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  233: "JS_GENERIC_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  234: "JS_UINT8_ARRAY_VALUE_ITERATOR_TYPE",
  235: "JS_INT8_ARRAY_VALUE_ITERATOR_TYPE",
  236: "JS_UINT16_ARRAY_VALUE_ITERATOR_TYPE",
  237: "JS_INT16_ARRAY_VALUE_ITERATOR_TYPE",
  238: "JS_UINT32_ARRAY_VALUE_ITERATOR_TYPE",
  239: "JS_INT32_ARRAY_VALUE_ITERATOR_TYPE",
  240: "JS_FLOAT32_ARRAY_VALUE_ITERATOR_TYPE",
  241: "JS_FLOAT64_ARRAY_VALUE_ITERATOR_TYPE",
  242: "JS_UINT8_CLAMPED_ARRAY_VALUE_ITERATOR_TYPE",
  243: "JS_FAST_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  244: "JS_FAST_HOLEY_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  245: "JS_FAST_ARRAY_VALUE_ITERATOR_TYPE",
  246: "JS_FAST_HOLEY_ARRAY_VALUE_ITERATOR_TYPE",
  247: "JS_FAST_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  248: "JS_FAST_HOLEY_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  249: "JS_GENERIC_ARRAY_VALUE_ITERATOR_TYPE",
  250: "WASM_INSTANCE_TYPE",
  251: "WASM_MEMORY_TYPE",
  252: "WASM_MODULE_TYPE",
  253: "WASM_TABLE_TYPE",
  254: "JS_BOUND_FUNCTION_TYPE",
  255: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x02201: (138, "FreeSpaceMap"),
  0x02251: (132, "MetaMap"),
  0x022a1: (131, "NullMap"),
  0x022f1: (171, "FixedArrayMap"),
  0x02341: (149, "OnePointerFillerMap"),
  0x02391: (149, "TwoPointerFillerMap"),
  0x023e1: (131, "UninitializedMap"),
  0x02431: (8, "OneByteInternalizedStringMap"),
  0x02481: (131, "UndefinedMap"),
  0x024d1: (129, "HeapNumberMap"),
  0x02521: (131, "TheHoleMap"),
  0x02571: (131, "BooleanMap"),
  0x025c1: (136, "ByteArrayMap"),
  0x02611: (171, "FixedCOWArrayMap"),
  0x02661: (172, "HashTableMap"),
  0x026b1: (128, "SymbolMap"),
  0x02701: (72, "OneByteStringMap"),
  0x02751: (171, "ScopeInfoMap"),
  0x027a1: (176, "SharedFunctionInfoMap"),
  0x027f1: (133, "CodeMap"),
  0x02841: (171, "FunctionContextMap"),
  0x02891: (177, "CellMap"),
  0x028e1: (178, "WeakCellMap"),
  0x02931: (179, "GlobalPropertyCellMap"),
  0x02981: (135, "ForeignMap"),
  0x029d1: (174, "TransitionArrayMap"),
  0x02a21: (173, "FeedbackVectorMap"),
  0x02a71: (131, "ArgumentsMarkerMap"),
  0x02ac1: (131, "ExceptionMap"),
  0x02b11: (131, "TerminationExceptionMap"),
  0x02b61: (131, "OptimizedOutMap"),
  0x02bb1: (131, "StaleRegisterMap"),
  0x02c01: (171, "NativeContextMap"),
  0x02c51: (171, "ModuleContextMap"),
  0x02ca1: (171, "EvalContextMap"),
  0x02cf1: (171, "ScriptContextMap"),
  0x02d41: (171, "BlockContextMap"),
  0x02d91: (171, "CatchContextMap"),
  0x02de1: (171, "WithContextMap"),
  0x02e31: (171, "DebugEvaluateContextMap"),
  0x02e81: (171, "ScriptContextTableMap"),
  0x02ed1: (171, "DescriptorArrayMap"),
  0x02f21: (148, "FixedDoubleArrayMap"),
  0x02f71: (134, "MutableHeapNumberMap"),
  0x02fc1: (172, "OrderedHashMapMap"),
  0x03011: (172, "OrderedHashSetMap"),
  0x03061: (172, "NameDictionaryMap"),
  0x030b1: (172, "GlobalDictionaryMap"),
  0x03101: (172, "NumberDictionaryMap"),
  0x03151: (172, "StringTableMap"),
  0x031a1: (172, "WeakHashTableMap"),
  0x031f1: (171, "SloppyArgumentsElementsMap"),
  0x03241: (180, "SmallOrderedHashMapMap"),
  0x03291: (181, "SmallOrderedHashSetMap"),
  0x032e1: (182, "CodeDataContainerMap"),
  0x03331: (189, "JSMessageObjectMap"),
  0x03381: (192, "ExternalMap"),
  0x033d1: (137, "BytecodeArrayMap"),
  0x03421: (171, "ModuleInfoMap"),
  0x03471: (177, "NoClosuresCellMap"),
  0x034c1: (177, "OneClosureCellMap"),
  0x03511: (177, "ManyClosuresCellMap"),
  0x03561: (175, "PropertyArrayMap"),
  0x035b1: (130, "BigIntMap"),
  0x03601: (106, "NativeSourceStringMap"),
  0x03651: (64, "StringMap"),
  0x036a1: (73, "ConsOneByteStringMap"),
  0x036f1: (65, "ConsStringMap"),
  0x03741: (77, "ThinOneByteStringMap"),
  0x03791: (69, "ThinStringMap"),
  0x037e1: (67, "SlicedStringMap"),
  0x03831: (75, "SlicedOneByteStringMap"),
  0x03881: (66, "ExternalStringMap"),
  0x038d1: (82, "ExternalStringWithOneByteDataMap"),
  0x03921: (74, "ExternalOneByteStringMap"),
  0x03971: (98, "ShortExternalStringMap"),
  0x039c1: (114, "ShortExternalStringWithOneByteDataMap"),
  0x03a11: (0, "InternalizedStringMap"),
  0x03a61: (2, "ExternalInternalizedStringMap"),
  0x03ab1: (18, "ExternalInternalizedStringWithOneByteDataMap"),
  0x03b01: (10, "ExternalOneByteInternalizedStringMap"),
  0x03b51: (34, "ShortExternalInternalizedStringMap"),
  0x03ba1: (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x03bf1: (42, "ShortExternalOneByteInternalizedStringMap"),
  0x03c41: (106, "ShortExternalOneByteStringMap"),
  0x03c91: (140, "FixedUint8ArrayMap"),
  0x03ce1: (139, "FixedInt8ArrayMap"),
  0x03d31: (142, "FixedUint16ArrayMap"),
  0x03d81: (141, "FixedInt16ArrayMap"),
  0x03dd1: (144, "FixedUint32ArrayMap"),
  0x03e21: (143, "FixedInt32ArrayMap"),
  0x03e71: (145, "FixedFloat32ArrayMap"),
  0x03ec1: (146, "FixedFloat64ArrayMap"),
  0x03f11: (147, "FixedUint8ClampedArrayMap"),
  0x03f61: (165, "Tuple2Map"),
  0x03fb1: (158, "ScriptMap"),
  0x04001: (153, "InterceptorInfoMap"),
  0x04051: (150, "AccessorInfoMap"),
  0x040a1: (151, "AccessorPairMap"),
  0x040f1: (152, "AccessCheckInfoMap"),
  0x04141: (154, "FunctionTemplateInfoMap"),
  0x04191: (155, "ObjectTemplateInfoMap"),
  0x041e1: (156, "AllocationSiteMap"),
  0x04231: (157, "AllocationMementoMap"),
  0x04281: (159, "AliasedArgumentsEntryMap"),
  0x042d1: (160, "PromiseResolveThenableJobInfoMap"),
  0x04321: (161, "PromiseReactionJobInfoMap"),
  0x04371: (162, "DebugInfoMap"),
  0x043c1: (163, "StackFrameInfoMap"),
  0x04411: (164, "PrototypeInfoMap"),
  0x04461: (166, "Tuple3Map"),
  0x044b1: (167, "ContextExtensionMap"),
  0x04501: (168, "ModuleMap"),
  0x04551: (169, "ModuleInfoEntryMap"),
  0x045a1: (170, "AsyncGeneratorRequestMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x02201): "NullValue",
  ("OLD_SPACE", 0x02231): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x02251): "EmptyFixedArray",
  ("OLD_SPACE", 0x02261): "UninitializedValue",
  ("OLD_SPACE", 0x022e1): "UndefinedValue",
  ("OLD_SPACE", 0x02311): "NanValue",
  ("OLD_SPACE", 0x02321): "TheHoleValue",
  ("OLD_SPACE", 0x02371): "HoleNanValue",
  ("OLD_SPACE", 0x02381): "TrueValue",
  ("OLD_SPACE", 0x023f1): "FalseValue",
  ("OLD_SPACE", 0x02441): "empty_string",
  ("OLD_SPACE", 0x02459): "EmptyScopeInfo",
  ("OLD_SPACE", 0x02469): "ArgumentsMarker",
  ("OLD_SPACE", 0x024c1): "Exception",
  ("OLD_SPACE", 0x02519): "TerminationException",
  ("OLD_SPACE", 0x02579): "OptimizedOut",
  ("OLD_SPACE", 0x025d1): "StaleRegister",
  ("OLD_SPACE", 0x02651): "EmptyByteArray",
  ("OLD_SPACE", 0x02661): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x02681): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x026a1): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x026c1): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x026e1): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x02701): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x02721): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x02741): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x02761): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x02781): "EmptyScript",
  ("OLD_SPACE", 0x02809): "UndefinedCell",
  ("OLD_SPACE", 0x02819): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x02839): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x02881): "EmptyOrderedHashMap",
  ("OLD_SPACE", 0x028a9): "EmptyOrderedHashSet",
  ("OLD_SPACE", 0x028d1): "EmptyPropertyCell",
  ("OLD_SPACE", 0x028f9): "EmptyWeakCell",
  ("OLD_SPACE", 0x02969): "NoElementsProtector",
  ("OLD_SPACE", 0x02991): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x029a1): "SpeciesProtector",
  ("OLD_SPACE", 0x029c9): "StringLengthProtector",
  ("OLD_SPACE", 0x029d9): "FastArrayIterationProtector",
  ("OLD_SPACE", 0x029e9): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02a11): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02a39): "InfinityValue",
  ("OLD_SPACE", 0x02a49): "MinusZeroValue",
  ("OLD_SPACE", 0x02a59): "MinusInfinityValue",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
)

# This set of constants is generated from a shipping build.
